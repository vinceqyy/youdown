from pytube import YouTube
from pytube import Playlist
import threading
import time


list_url = 'https://www.youtube.com/playlist?list=PLHnSLOMOPT11njaNmENJN6p2ro9MTc7t_'

p = Playlist(list_url)
download_path = 'D:/youtube/' +  p.title

def list_down(url):
    yt = YouTube(url)
    til = yt.title
    print('downloading '+ til)
    stream = yt.streams.get_highest_resolution()
    stream.download(download_path)

def single_thread():
    for url in p.video_urls:
        list_down(url)

def multi_thread():
    threads = []
    for url in p.video_urls:
        threads.append(threading.Thread(target=list_down, args = (url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start = time.time()
    multi_thread()
    end = time.time()
    print('cost:', end - start, 'Second')
    print('download completed')