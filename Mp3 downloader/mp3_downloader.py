from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def mp3Downloader():
    video_url = input("Enter the YouTube video URL: ")

    music_folder = "Musics"
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)

    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    video_path = stream.download()

    video_title = yt.title

    mp3_filename = os.path.join(music_folder, f"{video_title}.mp3")

    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_filename)

    video_clip.close()
    audio_clip.close()

    os.remove(video_path)

    print(f"Video '{video_title}' converted to MP3 successfully!")

while True:
    mp3Downloader()
