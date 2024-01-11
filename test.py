from pytube import YouTube
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()

link = simpledialog.askstring("YT-Video/Audio-Downloader", "Paste Link here")
yt = YouTube(link)

messagebox.showinfo(link,yt.title)
doa = simpledialog.askinteger("YT-Video/Audio-Downloader", "Press 1 to download audio only or 2 to download video")

try:
    if doa == 1:
        messagebox.showinfo("Downloading...","Downloading started please don't close this program")
        video = yt.streams.get_audio_only()
        curr_dir = os.getcwd()
        os.chdir(curr_dir)
        video.download()
        messagebox.showinfo("Downloading Finished!!","Downloaded!!")
    elif doa == 2:
        messagebox.showinfo("Downloading...","Downloading started don't close this program")
        video = yt.streams.get_by_resolution("")
        curr_dir = os.getcwd()
        os.chdir(curr_dir)
        video.download()
        messagebox.showinfo("Downloading Finished!!","Downloaded!!")
    else:
        messagebox.showinfo("Oops!","Enter valid input")


except Exception as e:
    print(e)