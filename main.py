import tkinter as tk
import customtkinter as ctk
from pytube import YouTube as yt
from yt_dlp import YoutubeDL


class YouTubeDownloader:
    def __init__(self, link):
        self.link = link
        self.ydl = YoutubeDL()

    def download_video(self):
        try:
            self.ydl.download([self.link])  # Download using yt-dlp
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


class YouTubeDownloaderApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("720x420")
        self.master.title("YouTube Downloader")

        # Create UI elements
        self.title_label = ctk.CTkLabel(self.master, text="Insert a YouTube URL")
        self.title_label.pack(padx=10, pady=10)

        self.url_var = tk.StringVar()
        self.url_entry = ctk.CTkEntry(self.master, width=350, height=40, textvariable=self.url_var)
        self.url_entry.pack()

        self.finished_label = ctk.CTkLabel(self.master, text="")
        self.finished_label.pack()

        self.download_button = ctk.CTkButton(self.master, text="Download", command=self.start_download)
        self.download_button.pack(padx=20, pady=20)

    def start_download(self):
        url = self.url_var.get()
        downloader = YouTubeDownloader(url)

        if downloader.download_video():
            self.finished_label.configure(text="Downloaded!", text_color="red")
        else:
            self.finished_label.configure(text="Download Error!", text_color="red")


# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Run the application
if __name__ == "__main__":
    root = ctk.CTk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
