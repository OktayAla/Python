import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Tensorflow kütüphanesi uyarısını kapatmak için
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model, save_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import logging
from pathlib import Path

# Loglama ayarları
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='jarfe_trading.log'
)


class JarfeTradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JarfeTrading")
        self.root.geometry("800x600")

        # Model ve veri depolama
        self.data = None
        self.model = None
        self.scaler = None
        self.model_path = Path("models")
        self.model_path.mkdir(exist_ok=True)

        self.create_gui()

    def create_gui(self):
        """GUI bileşenlerini oluştur"""
        # Ana frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Sol panel - Kontroller
        control_frame = ttk.LabelFrame(main_frame, text="Kontrol Paneli", padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # Para birimi girişi
        ttk.Label(control_frame, text="Para Birimi:").pack(pady=(0, 5), anchor=tk.W)
        self.ticker_entry = ttk.Entry(control_frame, width=20)
        self.ticker_entry.pack(pady=(0, 10), fill=tk.X)
        self.ticker_entry.insert(0, "EURUSD")

        # Dönem seçimi
        ttk.Label(control_frame, text="Dönem:").pack(pady=(0, 5), anchor=tk.W)
        self.period_combobox = ttk.Combobox(control_frame,
                                            values=["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd",
                                                    "max"])
        self.period_combobox.pack(pady=(0, 10), fill=tk.X)
        self.period_combobox.set("1mo")

        # Aralık seçimi
        ttk.Label(control_frame, text="Aralık:").pack(pady=(0, 5), anchor=tk.W)
        self.interval_combobox = ttk.Combobox(control_frame,
                                              values=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d",
                                                      "1wk", "1mo", "3mo"])
        self.interval_combobox.pack(pady=(0, 10), fill=tk.X)
        self.interval_combobox.set("1h")

        # Model parametre ayarları
        ttk.Label(control_frame, text="Epoch Sayısı:").pack(pady=(0, 5), anchor=tk.W)
        self.epochs_spinbox = ttk.Spinbox(control_frame, from_=1, to=100, increment=1)
        self.epochs_spinbox.pack(pady=(0, 10), fill=tk.X)
        self.epochs_spinbox.set("10")

        ttk.Label(control_frame, text="Batch Size:").pack(pady=(0, 5), anchor=tk.W)
        self.batch_spinbox = ttk.Spinbox(control_frame, from_=8, to=128, increment=8)
        self.batch_spinbox.pack(pady=(0, 10), fill=tk.X)
        self.batch_spinbox.set("32")

        # Stop Loss ve Take Profit yüzdeleri
        ttk.Label(control_frame, text="Stop Loss %:").pack(pady=(0, 5), anchor=tk.W)
        self.sl_spinbox = ttk.Spinbox(control_frame, from_=0.005, to=0.05, increment=0.005, format="%.3f")
        self.sl_spinbox.pack(pady=(0, 10), fill=tk.X)
        self.sl_spinbox.set("0.010")

        ttk.Label(control_frame, text="Take Profit %:").pack(pady=(0, 5), anchor=tk.W)
        self.tp_spinbox = ttk.Spinbox(control_frame, from_=0.01, to=0.1, increment=0.01, format="%.3f")
        self.tp_spinbox.pack(pady=(0, 10), fill=tk.X)
        self.tp_spinbox.set("0.020")

        # Butonlar
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(pady=10, fill=tk.X)

        ttk.Button(button_frame, text="Veri Çek", command=self.fetch_and_display).pack(side=tk.LEFT, padx=(0, 5),
                                                                                       fill=tk.X, expand=True)
        ttk.Button(button_frame, text="Analiz Yap", command=self.analyze).pack(side=tk.RIGHT, fill=tk.X, expand=True)

        # Model kaydetme/yükleme butonları
        model_button_frame = ttk.Frame(control_frame)
        model_button_frame.pack(pady=10, fill=tk.X)

        ttk.Button(model_button_frame, text="Modeli Kaydet", command=self.save_model).pack(side=tk.LEFT, padx=(0, 5),
                                                                                           fill=tk.X, expand=True)
        ttk.Button(model_button_frame, text="Modeli Yükle", command=self.load_model).pack(side=tk.RIGHT, fill=tk.X,
                                                                                          expand=True)

        # Sağ panel - Görselleştirme ve sonuçlar
        viz_frame = ttk.LabelFrame(main_frame, text="Görselleştirme ve Sonuçlar", padding="10")
        viz_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Grafik alanı
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Sonuç panel alanı
        self.result_text = tk.Text(viz_frame, height=10, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, pady=(10, 0), expand=True)

        # Durum çubuğu
        self.status_var = tk.StringVar()
        self.status_var.set("Hazır")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def fetch_and_display(self):
        """Verileri çek ve görselleştir"""
        try:
            self.status_var.set("Veriler çekiliyor...")
            self.root.update_idletasks()

            ticker = self.ticker_entry.get().strip()
            period = self.period_combobox.get()
            interval = self.interval_combobox.get()

            if not ticker:
                messagebox.showerror("Giriş Hatası", "Para birimi girilmedi.")
                return

            # Verileri çek
            self.data = self.fetch_data(ticker, period, interval)
            if self.data is None or self.data.empty:
                return

            # Grafik göster
            self.plot_data()
            self.status_var.set(f"{ticker} verileri başarıyla çekildi")

        except Exception as e:
            logging.error(f"Veri çekme hatası: {str(e)}")
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")
            self.status_var.set("Hata")

    def fetch_data(self, ticker, period="1mo", interval="1h"):
        """Veriyi Yahoo Finance'dan çeker."""
        try:
            if not ticker.endswith('=X'):
                ticker = ticker + '=X'

            logging.info(f"{ticker} için veri çekiliyor: period={period}, interval={interval}")
            data = yf.download(ticker, period=period, interval=interval)

            if data.empty:
                raise ValueError(f"{ticker} için veri bulunamadı.")

            # Eksik verileri doldur
            data = data.ffill().bfill()

            # EMA Hesaplamaları
            data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
            data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
            data['EMA_200'] = data['Close'].ewm(span=200, adjust=False).mean()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Veri başarıyla çekildi\n")
            self.result_text.insert(tk.END,
                                    f"Veri aralığı: {data.index[0].strftime('%Y-%m-%d %H:%M')} - {data.index[-1].strftime('%Y-%m-%d %H:%M')}\n")
            self.result_text.insert(tk.END, f"Toplam veri noktası: {len(data)}\n\n")

            return data

        except Exception as e:
            logging.error(f"Veri çekme hatası: {str(e)}")
            messagebox.showerror("Veri Hatası", f"Veri çekme sırasında bir hata oluştu: {e}")
            return None

    def plot_data(self):
        """Verileri görselleştirir"""
        if self.data is None:
            return

        self.ax.clear()

        # Kapanış fiyatları ve EMA'lar
        self.ax.plot(self.data.index, self.data['Close'], label='Kapanış Fiyatı', color='blue', alpha=0.5)
        self.ax.plot(self.data.index, self.data['EMA_20'], label='20 EMA', color='orange', linewidth=1)
        self.ax.plot(self.data.index, self.data['EMA_50'], label='50 EMA', color='green', linewidth=1)
        self.ax.plot(self.data.index, self.data['EMA_200'], label='200 EMA', color='red', linewidth=1)

        # Destek ve direnç seviyeleri
        window = 14
        support_levels = self.data['Close'].rolling(window=window).min()
        resistance_levels = self.data['Close'].rolling(window=window).max()

        self.ax.plot(self.data.index, support_levels, 'g--', alpha=0.7, label='Destek')
        self.ax.plot(self.data.index, resistance_levels, 'r--', alpha=0.7, label='Direnç')

        # Grafik özellikleri
        self.ax.set_title(f"{self.ticker_entry.get()} Fiyat Grafiği")
        self.ax.set_xlabel('Tarih')
        self.ax.set_ylabel('Fiyat')
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)
        plt.tight_layout()

        # Tarihleri düzenle
        self.fig.autofmt_xdate()

        self.canvas.draw()

    def identify_support_resistance(self, window=14):
        """Destek ve direnç seviyelerini belirler."""
        if self.data is None:
            return None, None

        rolling_min = self.data['Close'].rolling(window=window).min()
        rolling_max = self.data['Close'].rolling(window=window).max()

        return rolling_min, rolling_max

    def preprocess_data(self):
        """Veriyi ölçeklendirir ve hazırlık yapar."""
        if self.data is None:
            return None, None

        self.scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = self.scaler.fit_transform(self.data[['Close']])
        return scaled_data, self.scaler

    def create_model(self, input_shape):
        """LSTM modelini oluşturur."""
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def train_model(self, data):
        """Modeli verilen verilerle eğitir."""
        try:
            self.status_var.set("Model eğitiliyor...")
            self.root.update_idletasks()

            if len(data) < 60:
                messagebox.showwarning("Uyarı", "Eğitim için yeterli veri yok. En az 60 veri noktası gerekli.")
                return None

            x_train, y_train = [], []
            for i in range(60, len(data)):
                x_train.append(data[i - 60:i, 0])
                y_train.append(data[i, 0])

            x_train, y_train = np.array(x_train), np.array(y_train)

            if len(x_train) == 0:
                messagebox.showerror("Model Eğitimi Hatası", "Yeterli veri bulunamadı.")
                return None

            x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

            # Early stopping ekle
            early_stopping = EarlyStopping(
                monitor='loss',
                patience=3,
                restore_best_weights=True
            )

            # Model oluştur
            input_shape = (60, 1)
            self.model = self.create_model(input_shape)

            # Model eğitim parametreleri
            epochs = int(self.epochs_spinbox.get())
            batch_size = int(self.batch_spinbox.get())

            # Modeli eğit
            history = self.model.fit(
                x_train, y_train,
                epochs=epochs,
                batch_size=batch_size,
                callbacks=[early_stopping],
                verbose=1
            )

            # Eğitim kaybını görselleştir
            self.ax.clear()
            self.ax.plot(history.history['loss'])
            self.ax.set_title('Model Eğitim Kaybı')
            self.ax.set_ylabel('Kayıp')
            self.ax.set_xlabel('Epoch')
            self.ax.grid(True)
            self.canvas.draw()

            self.status_var.set("Model eğitimi tamamlandı")
            return self.model

        except Exception as e:
            logging.error(f"Model eğitimi hatası: {str(e)}")
            messagebox.showerror("Model Eğitimi Hatası", f"Model eğitilirken bir hata oluştu: {e}")
            self.status_var.set("Hata")
            return None

    def predict(self, data):
        """Model ile tahmin yapar."""
        try:
            if self.model is None:
                messagebox.showerror("Tahmin Hatası", "Önce modeli eğitmelisiniz.")
                return None

            # Veri tipini numpy array'e dönüştür
            if isinstance(data, pd.DataFrame):
                data = data.values

            test_data = data[-60:]
            inputs = self.scaler.transform(test_data)
            inputs = np.reshape(inputs, (1, inputs.shape[0], 1))
            predicted_price = self.model.predict(inputs)
            predicted_price = self.scaler.inverse_transform(predicted_price)

            # Skalar değere dönüştür
            return float(predicted_price[0][0])

        except Exception as e:
            logging.error(f"Tahmin hatası: {str(e)}")
            messagebox.showerror("Tahmin Hatası", f"Tahmin yaparken bir hata oluştu: {e}")
            return None

    def calculate_stop_loss_take_profit(self, current_price):
        """Stop Loss ve Take Profit seviyelerini hesaplar."""
        try:
            current_price = float(current_price)
            sl_percentage = float(self.sl_spinbox.get())
            tp_percentage = float(self.tp_spinbox.get())

            stop_loss = current_price * (1 - sl_percentage)
            take_profit = current_price * (1 + tp_percentage)

            return stop_loss, take_profit
        except Exception as e:
            logging.error(f"Stop Loss/Take Profit hesaplama hatası: {str(e)}")
            messagebox.showerror("Hata", f"Stop Loss/Take Profit hesaplanırken bir hata oluştu: {e}")
            return None, None

    def display_results(self, current_price, predicted_price, support, resistance,
                        stop_loss, take_profit, signal, ema_20, ema_50, ema_200):
        """Analiz sonuçlarını ekranda gösterir."""
        try:
            # Tüm değerlerin float tipinde olduğundan emin ol
            current_price = float(current_price)
            predicted_price = float(predicted_price)
            support = float(support)
            resistance = float(resistance)
            stop_loss = float(stop_loss)
            take_profit = float(take_profit)

            # Sonuç metnini temizle
            self.result_text.delete(1.0, tk.END)

            # Sonuçları ekle
            self.result_text.insert(tk.END, f"📊 ANALİZ SONUÇLARI\n\n")
            self.result_text.insert(tk.END, f"📈 Mevcut Fiyat: {current_price:.5f}\n")
            self.result_text.insert(tk.END, f"🔮 Tahmin Edilen Fiyat: {predicted_price:.5f}\n")

            # Değişim yüzdesi
            change_pct = ((predicted_price - current_price) / current_price) * 100
            direction = "artış" if change_pct > 0 else "düşüş"
            self.result_text.insert(tk.END, f"📊 Beklenen Değişim: %{abs(change_pct):.2f} {direction}\n\n")

            # Destek ve direnç seviyeleri
            self.result_text.insert(tk.END, f"🛑 Destek Seviyesi: {support:.5f}\n")
            self.result_text.insert(tk.END, f"🚫 Direnç Seviyesi: {resistance:.5f}\n\n")

            # Stop Loss ve Take Profit
            self.result_text.insert(tk.END, f"🛡️ Stop Loss: {stop_loss:.5f}\n")
            self.result_text.insert(tk.END, f"💰 Take Profit: {take_profit:.5f}\n\n")

            # Sinyal
            signal_emoji = "⚖️"
            if signal == "AL":
                signal_emoji = "🟢"
            elif signal == "SAT":
                signal_emoji = "🔴"

            self.result_text.insert(tk.END, f"{signal_emoji} İşlem Sinyali: {signal}\n")

            # İşlem tavsiyesi
            advice = ""
            if signal == "AL":
                advice = f"Alım fırsatı olabilir. Stop Loss: {stop_loss:.5f}, Take Profit: {take_profit:.5f}"
            elif signal == "SAT":
                advice = f"Satış fırsatı olabilir. Destek seviyesini ({support:.5f}) takip edin."
            else:
                advice = "Şu an için beklemede kalınabilir. Fiyat hareketlerini takip edin."

            self.result_text.insert(tk.END, f"💡 Tavsiye: {advice}\n")

            # EMA Değerleri
            self.result_text.insert(tk.END, f"\n📈 EMA Değerleri:\n")
            self.result_text.insert(tk.END, f"20 EMA: {ema_20:.5f}\n")
            self.result_text.insert(tk.END, f"50 EMA: {ema_50:.5f}\n")
            self.result_text.insert(tk.END, f"200 EMA: {ema_200:.5f}\n")

            # Sinyal
            signal_emoji = "⚖️"
            if signal == "AL":
                signal_emoji = "🟢"
            elif signal == "SAT":
                signal_emoji = "🔴"

            self.result_text.insert(tk.END, f"{signal_emoji} İşlem Sinyali: {signal}\n")

            # Tarih bilgisi
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.result_text.insert(tk.END, f"\n⏰ Analiz Zamanı: {current_time}")
        except Exception as e:
            logging.error(f"Sonuç gösterme hatası: {str(e)}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Sonuçlar gösterilirken bir hata oluştu: {str(e)}")

    def update_prediction_chart(self, predicted_price):
        """Tahmin grafiğini günceller."""
        try:
            # Mevcut grafiği koruyarak yeni tahmin noktası ekle
            last_date = self.data.index[-1]
            next_date = last_date + pd.Timedelta(hours=1)  # Bir sonraki saat

            # Kapanış değerini skalar değere dönüştür
            last_close = float(self.data['Close'].iloc[-1])

            # Numpy array'den skalar değere dönüştür
            if isinstance(predicted_price, np.ndarray):
                predicted_price = float(predicted_price)

            # Tahmin noktasını grafiğe ekle
            self.ax.plot([last_date, next_date],
                         [last_close, predicted_price],
                         'g--o', label='Tahmin')

            # Grafik özelliklerini güncelle
            self.ax.legend()
            self.canvas.draw()
        except Exception as e:
            logging.error(f"Tahmin grafiği güncellenirken hata: {str(e)}")
            # Hatayı gösterme ama işlemi devam ettir
            pass

    def save_model(self):
        """Eğitilmiş modeli kaydeder."""
        try:
            if self.model is None:
                messagebox.showerror("Kaydetme Hatası", "Kaydedilecek eğitilmiş model bulunamadı.")
                return

            # Dosya adı iste
            ticker = self.ticker_entry.get().strip()
            default_filename = f"{ticker}_model_{datetime.datetime.now().strftime('%Y%m%d')}"

            filename = filedialog.asksaveasfilename(
                initialdir=self.model_path,
                title="Modeli Kaydet",
                initialfile=default_filename,
                defaultextension=".h5",
                filetypes=[("Keras Model", "*.h5")]
            )

            if not filename:
                return

            # Modeli kaydet
            self.model.save(filename)

            # Scaler'ı pickle olarak kaydet
            if self.scaler is not None:
                scaler_filename = filename.replace(".h5", "_scaler.pkl")
                import pickle
                with open(scaler_filename, 'wb') as f:
                    pickle.dump(self.scaler, f)

            messagebox.showinfo("Başarılı", f"Model başarıyla kaydedildi:\n{filename}")
            self.status_var.set(f"Model kaydedildi: {filename}")

        except Exception as e:
            logging.error(f"Model kaydetme hatası: {str(e)}")
            messagebox.showerror("Kaydetme Hatası", f"Model kaydedilirken bir hata oluştu: {e}")

    def load_model(self):
        """Kaydedilmiş modeli yükler."""
        try:
            # Dosya seç
            filename = filedialog.askopenfilename(
                initialdir=self.model_path,
                title="Model Yükle",
                filetypes=[("Keras Model", "*.h5")]
            )

            if not filename:
                return

            # Modeli yükle
            self.model = load_model(filename)

            # Scaler'ı yükle
            scaler_filename = filename.replace(".h5", "_scaler.pkl")
            if os.path.exists(scaler_filename):
                import pickle
                with open(scaler_filename, 'rb') as f:
                    self.scaler = pickle.load(f)

            messagebox.showinfo("Başarılı", f"Model başarıyla yüklendi:\n{filename}")
            self.status_var.set(f"Model yüklendi: {filename}")

        except Exception as e:
            logging.error(f"Model yükleme hatası: {str(e)}")
            messagebox.showerror("Yükleme Hatası", f"Model yüklenirken bir hata oluştu: {e}")

    def analyze(self):
        """Kullanıcının seçtiği değerlerle veriyi analiz eder."""
        try:
            self.status_var.set("Analiz yapılıyor...")
            self.root.update_idletasks()

            if self.data is None:
                ticker = self.ticker_entry.get().strip()
                period = self.period_combobox.get()
                interval = self.interval_combobox.get()

                if not ticker:
                    messagebox.showerror("Giriş Hatası", "Para birimi girilmedi.")
                    return

                self.data = self.fetch_data(ticker, period, interval)
                if self.data is None or self.data.empty:
                    return

            # Veri görselleştirme
            self.plot_data()

            # Destek ve direnç seviyeleri
            support_levels, resistance_levels = self.identify_support_resistance()
            if support_levels is None or resistance_levels is None:
                messagebox.showerror("Destek/Direnç Hatası",
                                     "Destek ve direnç seviyeleri belirlenirken bir hata oluştu.")
                return

            # Veri ön işleme
            scaled_data, scaler = self.preprocess_data()
            if scaled_data is None or scaler is None:
                return

            # Model eğitimi
            if self.model is None:
                self.model = self.train_model(scaled_data)
                if self.model is None:
                    return

            # Tahmin
            predicted_price = self.predict(self.data[['Close']].values)
            if predicted_price is None:
                return

            # Güncel değerler - float dönüşümlerini burada yapıyoruz
            try:
                current_price = float(self.data['Close'].iloc[-1])
                latest_support = float(support_levels.dropna().iloc[-1])
                latest_resistance = float(resistance_levels.dropna().iloc[-1])
            except Exception as e:
                messagebox.showerror("Değer Hatası", f"Değerler işlenirken bir hata oluştu: {e}")
                return

            # Stop Loss ve Take Profit hesaplama
            stop_loss_price, take_profit_price = self.calculate_stop_loss_take_profit(current_price)
            if stop_loss_price is None or take_profit_price is None:
                return

            # Alım/satım sinyali belirleme
            signal = "NÖTR"
            if predicted_price > current_price * 1.01:  # %1'den fazla artış beklentisi
                signal = "AL"
            elif predicted_price < current_price * 0.99:  # %1'den fazla düşüş beklentisi
                signal = "SAT"

            # EMA değerlerini al
            ema_20 = float(self.data['EMA_20'].iloc[-1])
            ema_50 = float(self.data['EMA_50'].iloc[-1])
            ema_200 = float(self.data['EMA_200'].iloc[-1])

            # Sonuçları göster
            self.display_results(current_price, predicted_price, latest_support,
                                 latest_resistance, stop_loss_price, take_profit_price,
                                 signal, ema_20, ema_50, ema_200)

            # Tahmin grafiğini güncelle
            self.update_prediction_chart(predicted_price)

            self.status_var.set("Analiz tamamlandı")

        except Exception as e:
            logging.error(f"Analiz hatası: {str(e)}")
            messagebox.showerror("Analiz Hatası", f"Analiz yapılırken bir hata oluştu: {e}")
            self.status_var.set("Hata")


# Ana uygulamayı başlat
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = JarfeTradingApp(root)
        root.mainloop()
    except Exception as e:
        logging.critical(f"Uygulama çalıştırma hatası: {str(e)}")
        messagebox.showerror("Kritik Hata", f"Uygulama başlatılırken bir hata oluştu: {e}")