# import subprocess
# subprocess.call(["pip","install","youtube-dl"])
import youtube_dl

ydl_opos={
    'format':'bestvideo+bestaudio/best',
    'playlist_start': 10,
    'playlist_end': -1,
}
with youtube_dl.YoutubeDL(ydl_opos) as ydl:
    ydl.download(['https://youtube.com/playlist?list=PLhpS3tgUDZcrs5jESWwon8hFrblSYT30C&si=yW_fs_tEVxccWxsM'])