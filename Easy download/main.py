import yt_dlp
import os

video_url = 'https://www.youtube.com/shorts/ss8Q1coPduk'

# Get the path to the user's Desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
output_path = os.path.join(desktop_path, 'twitter2_video.mp4')

ydl_opts = {
    'format': 'best',
    'outtmpl': output_path,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print(f"Video downloaded to: {output_path}")


