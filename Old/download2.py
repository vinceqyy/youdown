from pytube import YouTube
from pytube import Playlist
import pandas as pd

list_url = 'https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'

url_data = pd.DataFrame()
p = Playlist(list_url)
for url in p.video_urls:
    yt = YouTube(url)
    til = yt.title
    lt = p.title
    data = pd.DataFrame({'Playlist': lt,'Link': url,'Title': til }, index=[0])
    url_data =url_data.append(data,ignore_index=True)
    #url_data = url_data.append(,ignore_index=True)

   
url_data.to_csv('download.csv')
    
#for video in p.videos:
#    stream = video.streams.filter(progressive=True).get_highest_resolution()
#    stream.download()

    #print(video.streams.filter(progressive= True))
    # yt.streams.filter(progressive=True)
    # video.streams.first().download()