from pytube import YouTube
from pytube import Playlist
from pytube import Channel
import pandas as pd

channel_url = 'https://www.youtube.com/channel/UCqEdIqFC2uQA9UD6yDaMeag/videos'

c = Channel(channel_url)
url_data = pd.DataFrame()
download_path = 'D:/youtube/' + c.channel_name
for url in c.video_urls:
    yt = YouTube(url)
    til = yt.title
    lt = c.channel_name
    try:
        print('downloading '+ til)
        stream = yt.streams.get_highest_resolution()
        stream.download(download_path)
        mg = 'Success'
    except:
        mg = 'Failed'
    data = pd.DataFrame({'Playlist': lt,'Link': url,'Title': til,'Status': mg}, index=[0])
    url_data =url_data.append(data,ignore_index=True)

   
url_data.to_csv('download.csv')
print('download completed') 