import customtkinter as ctk
import os
import yt_dlp
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow kütüphanesini import et

# Genel tanımlamalar
class PyDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("pyDownloader | Youtube MP3 Downloader | OA")
        self.geometry("600x250")
        self.resizable(False, False)
        ctk.set_appearance_mode("Light")  # Açık tema
        ctk.set_default_color_theme("blue")
        self.video_link = ctk.StringVar()
        self.create_widgets()

# Widget'ları oluştur
    def create_widgets(self):
        # Logo
        self.logo_img = ctk.CTkImage(Image.open("logo.png"), size=(380, 80))
        self.logo_label = ctk.CTkLabel(self, image=self.logo_img, text="")
        self.logo_label.pack(pady=(20, 10))

        # Link Giriş Alanı
        self.link_frame = ctk.CTkFrame(self)
        self.link_frame.pack(pady=10, padx=20, fill="x")

        self.videolink_label = ctk.CTkLabel(self.link_frame, text="Youtube Link:", width=100)
        self.videolink_label.pack(side="left", padx=(10, 0))

        self.videolink_textbox = ctk.CTkEntry(self.link_frame, textvariable=self.video_link, width=350)
        self.videolink_textbox.pack(side="left", fill="x", expand=True, padx=10)

        # İndirme Butonu
        self.indir_button = ctk.CTkButton(self, text="İndir", command=self.indir, font=ctk.CTkFont(size=16, weight="bold"), fg_color="red", hover_color="#8B0000")
        self.indir_button.pack(pady=20)

        # Durum Mesajı
        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.pack(pady=(0, 10))

# İndirme İşlemi
    def indir(self):
        youtube_link = self.video_link.get()

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio',
            'outtmpl': os.path.join(desktop_path, '%(title)s.mp3'),
            'noplaylist': True,
        }

        try:
            self.status_label.configure(text="İndiriliyor...", text_color="orange")
            self.update()

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_link])

            messagebox.showinfo("Başarılı", "Dosya başarıyla masaüstüne indirildi.")
            self.status_label.configure(text="İndirme Tamamlandı", text_color="green")
        except Exception as e:
            messagebox.showerror("Hata", f"İndirme sırasında bir hata oluştu: {str(e)}")
            self.status_label.configure(text=f"Hata: {str(e)}", text_color="red")
        finally:
            self.update()

if __name__ == "__main__":
    app = PyDownloader()
    app.mainloop()