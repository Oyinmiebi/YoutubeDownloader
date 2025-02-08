from pytube import YouTube

link = input() # https://www.youtube.com/watch?v=RJVCu1wFbJk

yt = YouTube(link)
mp4 = yt.streams.filter(file_extension="mp4").all()

mp4.download()