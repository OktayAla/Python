import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from pytube import YouTube
import os
from PIL import ImageTk, Image

PyDownloader=tk.Tk()
PyDownloader.title("pyDownloader | Youtube MP3 Downloader | OA")
PyDownloader.geometry("440x220")

img = ImageTk.PhotoImage(Image.open("Logo.png"))
panel = Label(PyDownloader, image = img)
panel.pack()

def dosyakonumu():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    download_Path.set(download_Directory)

def indir():
    youtube_link = video_Link.get()
    indirme_konumu = download_Path.get()
    getVideo = YouTube(youtube_link)

    videoStream = getVideo.streams.filter(only_audio=True).first()
    videoStreams=videoStream.download(indirme_konumu)

    base, ext = os.path.splitext(videoStreams)
    to_mp3 = base + ".mp3"
    os.rename(videoStreams, to_mp3)

    messagebox.showinfo("Başarılı","Dosya başarıyla indirildi.")


video_Link = StringVar()
download_Path = StringVar()

videolink_label = tk.Label(text="Youtube Link:",font="Arial 10 bold")
videolink_label.place(x=10,y=80)

videolink_textbox = tk.Entry(PyDownloader, textvariable = video_Link)
videolink_textbox.place(x=120,y=80,width=310,height=30)

dosyakonumu_label = tk.Label(text="Dosya Konumu:",font="Arial 10 bold")
dosyakonumu_label.place(x=10,y=135)

dosyakonumu_textbox = tk.Entry(PyDownloader, textvariable = download_Path)
dosyakonumu_textbox.place(x=120,y=130,width=310,height=30)

indir_buton=tk.Button(text="İndir",
                      command=indir,
                      font="Arial 13 bold",
                      bg="darkred",fg="white")
indir_buton.place(x=150, y=170)
indir_buton.configure()

dosyakonumu_buton=tk.Button(text="Konum seç",
                            command=dosyakonumu,
                            font="Arial 13 bold",
                            bg="darkred",fg="white")
dosyakonumu_buton.place(x=10, y=170)
dosyakonumu_buton.configure()


PyDownloader.mainloop()