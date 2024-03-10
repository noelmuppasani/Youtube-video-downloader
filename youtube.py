from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path, filename='video.mp4')
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)


url = "https://www.youtube.com/watch?v=kVIQ5t8WUFk"
save_path = "C://Users//ACER//Downloads" 

download_video(url, save_path)
