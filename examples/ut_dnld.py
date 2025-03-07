from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=-VKT7p6TD6U")
yt = yt.streams.first().download('C:\\Users\\Kumars\\OneDrive\ -\ Edge\ Hill\ University\\CIS3138\\tkinter_tutorials')