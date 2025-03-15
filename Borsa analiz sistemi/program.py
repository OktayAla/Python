import yfinance as yf  # Yahoo Finance'dan veri çekmek için gerekli kütüphane
import pandas as pd  # Veri işleme ve analiz için pandas kütüphanesi
import numpy as np  # Nümerik işlemler için numpy kütüphanesi
from sklearn.preprocessing import MinMaxScaler  # Veriyi ölçeklendirmek için MinMaxScaler
from tensorflow.keras.models import Sequential  # Keras'tan model oluşturmak için Sequential sınıfı
from tensorflow.keras.layers import LSTM, Dense, Dropout
import tkinter as tk  # GUI (Grafiksel Kullanıcı Arayüzü) için tkinter kütüphanesi
from tkinter import messagebox
from tkinter import ttk


# Verileri Çekmek
def fetch_data(ticker, period="1mo", interval="1h"):
    """
    Veriyi Yahoo Finance'dan çeker.

    :param ticker: Para birimi sembolü (örneğin, 'EURUSD')
    :param period: Verinin kapsadığı dönem (örneğin, '1mo' bir ay)
    :param interval: Verinin aralığı (örneğin, '1h' bir saat)
    :return: Veriyi içeren bir DataFrame
    """
    try:
        if not ticker.endswith('=X'):
            ticker = ticker + '=X'  # Sembolün sonuna '=X' ekle
        data = yf.download(ticker, period=period, interval=interval)  # Yahoo Finance'dan veri çek
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker}.")  # Veri bulunamadıysa hata ver
        data = data[['Close']]  # Sadece kapanış fiyatlarını al
        return data
    except Exception as e:
        messagebox.showerror("Veri Hatası", f"Veri çekme sırasında bir hata oluştu: {e}")  # Hata mesajını göster
        return None


# Veri Ön İşleme
def preprocess_data(data):
    """
    Veriyi ölçeklendirir ve hazırlık yapar.

    :param data: Raw veri DataFrame'i
    :return: Ölçeklendirilmiş veri ve scaler nesnesi
    """
    scaler = MinMaxScaler(feature_range=(0, 1))  # Veriyi 0 ve 1 arasında ölçeklendirmek için scaler oluştur
    scaled_data = scaler.fit_transform(data)  # Veriyi ölçeklendir
    return scaled_data, scaler


# Destek ve Direnç Seviyelerini Belirleme
def identify_support_resistance(data, window=14):
    """
    Destek ve direnç seviyelerini belirler.

    :param data: Kapanış fiyatları içeren veri
    :param window: Kaydırmalı pencere boyutu
    :return: Destek ve direnç seviyeleri
    """
    rolling_max = data['Close'].rolling(window=window).max()  # Kaydırmalı pencere ile maksimum fiyatları al
    rolling_min = data['Close'].rolling(window=window).min()  # Kaydırmalı pencere ile minimum fiyatları al

    support_levels = rolling_min  # Destek seviyeleri minimum fiyatlar
    resistance_levels = rolling_max  # Direnç seviyeleri maksimum fiyatlar

    return support_levels, resistance_levels


# Makine öğrenmesi modeli
def create_model(input_shape):
    """
    LSTM modelini oluşturur.

    :param input_shape: Modelin giriş şekli
    :return: Oluşturulan model
    """
    model = Sequential()  # Sequential model oluştur
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))  # LSTM katmanı ekle
    model.add(Dropout(0.2))  # Overfitting'i önlemek için dropout ekle
    model.add(LSTM(units=50, return_sequences=False))  # İkinci LSTM katmanını ekle
    model.add(Dropout(0.2))  # Yine dropout ekle
    model.add(Dense(units=1))  # Çıkış katmanı
    model.compile(optimizer='adam', loss='mean_squared_error')  # Modeli 'adam' optimizer ile ve MSE kaybıyla derle
    return model


# Modeli eğitmek
def train_model(data, model):
    """
    Modeli verilen verilerle eğitir.

    :param data: Eğitim verisi
    :param model: Eğitilecek model
    :return: Eğitilmiş model
    """
    x_train, y_train = [], []  # Eğitim verileri için boş listeler oluştur
    for i in range(60, len(data)):  # 60 günün üzerinde verilerle eğitim yap
        x_train.append(data[i - 60:i, 0])  # Son 60 günün verisini x_train'e ekle
        y_train.append(data[i, 0])  # Gelecek günün kapanış fiyatını y_train'e ekle
    x_train, y_train = np.array(x_train), np.array(y_train)  # Listeleri numpy array'e dönüştür

    if len(x_train) == 0:  # Eğer yeterli veri yoksa hata mesajı göster
        messagebox.showerror("Model Eğitimi Hatası", "Yeterli veri bulunamadı.")
        return model

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))  # x_train'i uygun şekle getir
    model.fit(x_train, y_train, epochs=10, batch_size=32)  # Modeli 10 epoch ve 32 batch ile eğit
    return model


# Model tahmini
def predict(model, data, scaler):
    """
    Model ile tahmin yapar.

    :param model: Eğitimli model
    :param data: Tahmin yapılacak veri
    :param scaler: Verinin ölçeklendirilmiş hali
    :return: Tahmin edilen fiyat
    """
    test_data = data[-60:]  # Son 60 günün verisini al
    inputs = scaler.transform(test_data)  # Veriyi ölçeklendir
    inputs = np.reshape(inputs, (1, inputs.shape[0], 1))  # Veriyi uygun şekle getir
    predicted_price = model.predict(inputs)  # Model ile tahmin yap
    predicted_price = scaler.inverse_transform(predicted_price)  # Tahmini eski ölçeğine döndür
    return predicted_price


# Stop Loss ve Take Profit Hesaplama
def calculate_stop_loss_take_profit(current_price, support, resistance, stop_loss_percentage=0.01,
                                    take_profit_percentage=0.02):
    """
    Stop Loss ve Take Profit fiyatlarını hesaplar.

    :param current_price: Şu anki fiyat
    :param support: Destek seviyesi
    :param resistance: Direnç seviyesi
    :param stop_loss_percentage: Stop Loss yüzdesi
    :param take_profit_percentage: Take Profit yüzdesi
    :return: Stop Loss ve Take Profit fiyatları
    """
    stop_loss_price = current_price - (current_price * stop_loss_percentage)  # Stop Loss fiyatını hesapla
    take_profit_price = current_price + (current_price * take_profit_percentage)  # Take Profit fiyatını hesapla
    return stop_loss_price, take_profit_price


# Analiz Fonksiyonu
def analyze():
    """
    Kullanıcının seçtiği değerlerle veriyi analiz eder.
    """
    ticker = ticker_entry.get().strip()  # Kullanıcıdan alınan para birimi kodunu al
    period = period_combobox.get()  # Kullanıcıdan alınan period değerini al
    interval = interval_combobox.get()  # Kullanıcıdan alınan interval değerini al

    if not ticker:  # Eğer para birimi girilmemişse hata mesajı göster
        messagebox.showerror("Giriş Hatası", "Para birimi girilmedi.")
        return

    data = fetch_data(ticker, period, interval)  # Veriyi çek
    if data is None or data.empty:  # Eğer veri çekilemediyse veya veri boşsa, hata mesajı göster
        return

    support_levels, resistance_levels = identify_support_resistance(data)  # Destek ve direnç seviyelerini belirle
    if support_levels is None or resistance_levels is None:  # Eğer destek ve direnç seviyeleri belirlenememişse hata mesajı göster
        messagebox.showerror("Destek/Direnç Hatası", "Destek ve direnç seviyeleri belirlenirken bir hata oluştu.")
        return

    scaled_data, scaler = preprocess_data(data)  # Veriyi ölçeklendir
    input_shape = (60, 1)  # Modelin giriş şekli
    model = create_model(input_shape)  # Modeli oluştur
    model = train_model(scaled_data, model)  # Modeli eğit
    if model is None:  # Eğer model eğitilememişse işlemi bitir
        return

    predicted_price = predict(model, scaled_data, scaler)  # Model ile tahmin yap
    current_price = float(data['Close'].iloc[-1].iloc[0])  # Şu anki fiyatı al
    predicted_price = float(predicted_price[0][0])  # Tahmin edilen fiyatı al
    potential_buy_price = float(support_levels.dropna().iloc[-1].iloc[0])  # En son destek seviyesini al
    potential_sell_price = float(resistance_levels.dropna().iloc[-1].iloc[0])  # En son direnç seviyesini al

    # Stop Loss ve Take Profit Fiyatları
    stop_loss_price, take_profit_price = calculate_stop_loss_take_profit(current_price, potential_buy_price,
                                                                         potential_sell_price)

    # Analiz çıktıları
    messagebox.showinfo("Analiz Sonucu",
                        f"Mevcut Fiyat: {current_price:.5f}\n"  # Mevcut fiyatı göster
                        f"Tahmin Edilen Fiyat: {predicted_price:.5f}\n"  # Tahmin edilen fiyatı göster
                        f"Potansiyel Alış Fiyatı: {potential_buy_price:.5f}\n"  # Potansiyel alış fiyatını göster
                        f"Potansiyel Satış Fiyatı: {potential_sell_price:.5f}\n"  # Potansiyel satış fiyatını göster
                        f"Stop Loss Fiyatı: {stop_loss_price:.5f}\n"  # Stop Loss fiyatını göster
                        f"Take Profit Fiyatı: {take_profit_price:.5f}")  # Take Profit fiyatını göster


# Tkinter Arayüzü
root = tk.Tk()  # Ana pencereyi oluştur
root.title("JarfeTrading")  # Pencere başlığını ayarla

# Para birimi sembolü için textbox
tk.Label(root, text="Para Birimi:").pack(pady=5)  # Para birimi etiketi ekle
ticker_entry = tk.Entry(root)  # Para birimi girişi için textbox oluştur
ticker_entry.pack(pady=5)  # Textbox'u pencereye ekle

# Period seçim ComboBox
tk.Label(root, text="Dönem:").pack(pady=5)  # Dönem etiketi ekle
period_combobox = ttk.Combobox(root, values=["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"])
period_combobox.pack(pady=5)  # Period ComboBox'u pencereye ekle
period_combobox.set("1mo")  # Varsayılan değer olarak "1mo" seç

# Interval seçim ComboBox
tk.Label(root, text="Aralık:").pack(pady=5)  # Aralık etiketi ekle
interval_combobox = ttk.Combobox(root,
                                 values=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo",
                                         "3mo"])
interval_combobox.pack(pady=5)  # Interval ComboBox'u pencereye ekle
interval_combobox.set("1h")  # Varsayılan değer olarak "1h" seç

# Analiz butonu
analyze_button = tk.Button(root, text="Analiz Yap",
                           command=analyze)  # Analiz butonu oluştur ve analiz fonksiyonunu bağla
analyze_button.pack(pady=20)  # Butonu pencereye ekle

root.mainloop()  # Tkinter'ın ana döngüsünü başlat