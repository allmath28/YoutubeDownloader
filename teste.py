from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PL_FD7wbDO4ubhXgI3ku8MAs6bnCYrNbn7')



for video in p.videos:
    video.streams.get_audio_only().download()
    print(f'Downloading: {video.title}')