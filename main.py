# imports

import tkinter as tk
import customtkinter as ctk
from pytube import YouTube as yt
from yt_dlp import YoutubeDL

# functions
def startDownload():
    try:
        ytlink = url.get()
        #ytVideo = yt(ytlink) # an object of a YouTube video
        
        with YoutubeDL() as ydl:
            ydl.download(ytlink)
    
        #mp4 = ytVideo.streams.filter(file_extension="mp.4").all() # get only mp4 files
        #video = ytVideo.streams.get_lowest_resolution() #this is extra but it ensures we download the highest/lowest res per video
        #title.configure(text=ytVideo.title()) # Gets the video title and displays it 
        #video.download()
        
        finished.configure(text="Downloaded!", text_color="red")
        
    except:
        finished.configure(text="Download Error!", text_color="red")
        
    
    
    
# System settings

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# application frame, create an app object

app = ctk.CTk()
app.geometry("720x420")
app.title("YouTube Downloader")

# add UI elements
title = ctk.CTkLabel(app, text="Insert a YouTube url")
title.pack(padx=10, pady=10)

# Add a link
# add a variable to collect the url
url_var = tk.StringVar()

url = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
url.pack()

# Label to indicate download finished
finished = ctk.CTkLabel(app, text="")
finished.pack()

#download button
download = ctk.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20, pady=20) # adds the element to the ui




# Run app
app.mainloop()


