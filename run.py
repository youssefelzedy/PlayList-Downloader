import os
from pytube import Playlist


def make_alpha_numeric(string):
    return ''.join(char for char in string if char.isalnum())


def make_alpha_numeric_with_spaces(string):
    return ''.join(char for char in string if char.isalnum() or char.isspace())


link = input("Enter YouTube Playlist URL: ✨")

yt_playlist = Playlist(link)

folderName = make_alpha_numeric_with_spaces(yt_playlist.title)
os.mkdir(folderName)

totalVideoCount = len(yt_playlist.videos)
print("Total videos in playlist: 🎦", totalVideoCount)
digits1 = sum(1 for char in str(totalVideoCount) if char.isdigit())

for index, video in enumerate(yt_playlist.videos, start=1):
    digits2 = sum(1 for char in str(index) if char.isdigit())
    print("Downloading:", video.title)
    video_size = video.streams.get_by_resolution(resolution=480).filesize
    print("Size:", video_size // (1024 ** 2), "🗜 MB")
    video.streams.get_by_resolution(resolution=480).download(
        output_path=folderName, filename=("0"*(digits1 - digits2) + str(index) + " - " + make_alpha_numeric_with_spaces(video.title) + ".mp4"))
    print("Downloaded:", video.title, "✨ successfully!")
    print("Remaining Videos:", totalVideoCount - index)

print("All videos downloaded successfully! 🎉")

