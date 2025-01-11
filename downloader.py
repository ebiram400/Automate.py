import pytube

pytube_url="https://youtube.com/playlist?list=PLWET7RCU6edMDaoBPFWSGEiRM5xQe98_s&si=xW5EBeLN8ekAAe3o"
playlist=pytube.Playlist(pytube_url)
print(playlist.title)

for index,video in enumerate(playlist.videos):
    streams=video.streams.filter(resolution="360p")
    for stream in streams:
        stream.download()
        print(f"Downloaded {video.title}")