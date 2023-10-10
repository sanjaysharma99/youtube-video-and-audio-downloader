import pytube
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

base_path=os.getcwd()

def download_audio_and_video(video_url):
    global base_path
    yt=pytube.YouTube(video_url)
    video=yt.streams.get_highest_resolution()
    filename=video.download(output_path=os.path.join(base_path,'static/user_files'))

    videoclip=VideoFileClip(filename=filename)
    audioclip=videoclip.audio
    audioclip.write_audiofile(f'{filename}.mp3')
    videoclip.close()
    audioclip.close()

    return filename, f'{filename}.mp3'
