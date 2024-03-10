from pytube import YouTube
import tkinter as tk

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=SAVE_PATH, filename='video.mp4')
        status_label.config(text="Video downloaded successfully!")
    except Exception as error:
        status_label.config(text=str(error))

# Static destination path
SAVE_PATH = "C://Users//ACER//Downloads"  

# GUI Setup
root = tk.Tk()
root.title("YouTube Video Downloader")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()