from pytube import YouTube

# Video URL
video_url = 'https://www.youtube.com/watch?v=mbpW0EfqoHQ&list=LL&index=7'

try:
    # Youtube Object
    video = YouTube(video_url)
except VideoUnavailable:
    # if video is unavailble print error message 
    print(f'Video {video_url} is unavaialable, skipping.')
else:
    # Printing video information
    print(f"Title: {video.title}\nViews: {video.views}\nLength: {video.length} seconds")

    # Getting the highest resolution stream for both video and audio
    stream = video.streams.get_highest_resolution()

    # Define the download path
    download_path = 'C:/Users/Laptop/Desktop/Video-Downloader'

    # downloading the video
    stream.download(download_path)

    print("Download completed!")

