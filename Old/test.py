from pytube import YouTube
from pytube import Playlist
from pytube import Channel

url = 'https://www.youtube.com/watch?v=BsWSqpaaYRc&t=59s'

yt = YouTube(url)

stream = yt.streams.filter(only_audio= True, file_extension= 'mp4').get_audio_only()

stream.download()