from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video():
    url = url_entry.get()
    save_path = save_path_var.get()
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        status_label.config(text="Video downloaded successfully!")
    except Exception as e:
        status_label.config(text="An error has occured please try again(make sure to include a possible URL and Location)")


def choose_save_dir():
    folder = filedialog.askdirectory()
    if folder:
        save_path_var.set(folder)
        status_label.config(text=f"Selected folder: {folder}")


# Create main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL input
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Save directory selection
save_label = tk.Label(root, text="Select save directory:")
save_label.pack()
save_path_var = tk.StringVar()
save_path_entry = tk.Entry(root, textvariable=save_path_var, width=50)
save_path_entry.pack()
browse_button = tk.Button(root, text="Browse", command=choose_save_dir)
browse_button.pack()

# Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()