from pytube import YouTube
from pytube import Playlist

list_url = 'https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'

p = Playlist(list_url)
#for url in p.video_urls[:3]:
#    print(url)
for video in p.videos:
    stream = video.streams.filter(progressive=True).get_highest_resolution()
    stream.download()

    #print(video.streams.filter(progressive= True))
    # yt.streams.filter(progressive=True)
    # video.streams.first().download()