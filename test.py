# import pytube
# link = "https://www.youtube.com/watch?v=WKU2UrhqW7k" 
# yt = pytube.YouTube(link)
# stream = yt.streams.get_lowest_resolution()
# stream.download()


from yt_dlp import YoutubeDL
URLS = "https://www.youtube.com/watch?v=WKU2UrhqW7k"

with YoutubeDL() as ydl:
    ydl.download(URLS)