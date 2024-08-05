import yt_dlp
import os

# Replace this with the URL of the Twitter video you want to download
video_url = 'https://www.youtube.com/watch?v=sz9K1e3LO4M'

# Get the path to the user's Desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
output_path = os.path.join(desktop_path, '_video.mp4')

ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Download video up to 1080p
    'outtmpl': output_path,
    'merge_output_format': 'mp4',  # Ensure the output is in mp4 format
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Ensure the output is in mp4 format
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print(f"Video downloaded to: {output_path}")
