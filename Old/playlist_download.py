from pytube import YouTube
from pytube import Playlist
import pandas as pd

list_url = 'https://www.youtube.com/watch?v=J3SiyMingRk&list=PLHnSLOMOPT11njaNmENJN6p2ro9MTc7t_&index=1'


url_data = pd.DataFrame()
p = Playlist(list_url)
download_path = 'D:/youtube/' +  p.title
for url in p.video_urls:
    yt = YouTube(url)
    til = yt.title
    lt = p.title
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