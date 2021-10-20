from pytube import YouTube
link = input("enter the video link to download: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
print("downloading...")
ys.download = ('Downloads')

print("download completed!!")