import tkinter as tk
import tkinter
import pytube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *
import threading


# create the main window
root = Tk()
root.geometry("600x125")
root.title("Download&ADM")
root.configure(bg="#C5EA94")
root.resizable(height=FALSE, width=FALSE)
root.update_idletasks()
# root.iconbitmap(default='Download.ico')

# create the menubar
menubar = Menu(root)
root.config(menu=menubar)
flieMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=flieMenu)
flieMenu.add_command(label="Exit", command=quit)

# function to browse and select a folder for saving the downloaded file


def Browse_save():
    global folder_path
    folder_path = filedialog.askdirectory()

# function to download the video


def download_video(link):
    yt = pytube.YouTube(link)
    video = yt.streams.filter(resolution="720p").first()
    video.filename = "my_video"
    video.download(folder_path)


def start_download(link):
    # Start the download in a separate thread
    threading.Thread(target=download_video, args=(link,)).start()

# function to download the audio


def Audio():
    link2 = (ent1.get())
    data = pytube.YouTube(link2)
    audio = data.streams.get_audio_only()
    audio.download(folder_path)


def run_in_thread(function):
    thread = threading.Thread(target=function)
    thread.start()


# create the buttons
btn1 = tkinter.Button(root, command=lambda: start_download(ent1.get(
)), text="Video Download", width="20", font="Ivy 8 bold", height="2", bg="#399494")
btn2 = tkinter.Button(root, command=lambda: run_in_thread(
    Audio), text="Audio Downloading", width="20", font="Ivy 8 bold", height="2", bg="#57BC8D")
btn3 = tkinter.Button(root, command=Browse_save, text="---", width="2", font="Ivy 8 bold", height="1", bg="#DEE979")

# create the entry and label
ent1 = ttk.Entry(root,  width=50, justify=CENTER, font="Ivy 12 bold")
lab1 = tkinter.Label(root, text="Link", font="font-weight", bg="#C5EA94")
lab2 = tk.Label(text="Start Download File", font="font-weight", bg="#C5EA94")
lab3 = tk.Label(text="A.D-0.1.2", font="Ivy 8 bold", bg="#C5EA94")

# pack and place the widgets
ent1.pack()
ent1.place(x=76, y=30)
btn1.pack()
btn1.place(x=50, y=61)
btn2.pack()
btn2.place(x=400, y=60)
btn3.pack()
btn3.place(x=540, y=30)
lab1.pack()
lab1.place(x=35, y=31)
lab2.pack()
lab2.place(x=220, y=4)
lab3.place(x=5, y=109)
root.mainloop()
