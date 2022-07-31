from doctest import master
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from pytube import Playlist


root = tk.Tk()
root.geometry("400x250")
root.resizable(True, True)
root.title('Downloader')

# store playlist url
playlist = tk.StringVar()
playlist = str(playlist)
p = Playlist(playlist)


def download():
    for video in p.videos:
        video.streams.get_audio_only().download()
        

    


# link
playlist_label = ttk.Label(root, text="Link da playlist:")
playlist_label.pack(fill='x', expand=True)

playlist = ttk.Entry(root, textvariable=playlist)
playlist.pack(fill='x', expand=True)
playlist.focus()



# download button
download_button = ttk.Button(root, text="Download", command=download)
download_button.pack(fill='x', expand=True, pady=10)


root.mainloop()