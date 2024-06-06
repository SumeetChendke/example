import os
from pytube import YouTube, exceptions
from time import time
from tkinter import *
from customtkinter import *

# Initialize all the settings
set_appearance_mode("System")  # Setting the appearance mode to follow by the app: "System", "Light" or "Dark"
set_default_color_theme("blue")  # Setting the theme of the app to follow

# Create 'youtube_downloads' directory if it doesn't exist
if not os.path.exists("youtube_downloads"):
    os.mkdir("youtube_downloads")

# Download video function
def download_video(entry_field):
    try:
        start_time = time()
        download_location = "youtube_downloads/"
        YouTube(entry_field).streams.first().download(download_location)
        end_time = time()

        # Showing the download time and status in a new window
        popup = CTk()
        popup.title("Download Status")
        popup.resizable(False, False)
        popup.geometry("300x150")
        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure((0,1,2), weight=1)
        
        # Status Label
        status_label = CTkLabel(popup, text="Download successful!", font=("Helvetica", 12, "bold"), fg="green")
        status_label.grid(row=0, column=0, pady=10)
        
        # Download Time Label
        msg = StringVar(value=f"Total time taken: {round(end_time-start_time,3)} seconds")
        time_label = CTkLabel(popup, textvariable=msg, font=("Helvetica", 10), fg="black")
        time_label.grid(row=1, column=0, pady=5)

        # OK Button
        button = CTkButton(popup, text="OK", command=popup.destroy, bg="blue", fg="white")
        button.grid(row=2, column=0, pady=10)

        popup.mainloop()
    except exceptions.RegexMatchError: # If there's an invalid link or empty link, show an error message
        error = CTk()
        error.title("Error")
        error.resizable(False, False)
        error.geometry("300x100")
        error.grid_rowconfigure((0,1), weight=1)
        error.grid_columnconfigure(0, weight=1)
        error_label = CTkLabel(error, text="Please enter a valid YouTube link", font=("Helvetica", 12), fg="red")
        error_label.grid(row=0, column=0, pady=10)
        button = CTkButton(error, text="OK", command=error.destroy, bg="blue", fg="white")
        button.grid(row=1, column=0, pady=10)
        error.mainloop()

# Initializing the layout of the app
master = CTk()
master.title("YouTube Downloader")
master.grid_rowconfigure((0,1), weight=1)
master.grid_columnconfigure((0,1), weight=1)
master.geometry("350x150")
master.resizable(False, False)
master.config(bg="white")  # Set background color

# GUI elements
CTkLabel(master, text="Enter YouTube video URL:", font=("Helvetica", 12), fg="black", bg="white").grid(row=0, column=0, padx=10, pady=10)
entry = CTkEntry(master, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=10, pady=10)
CTkButton(master, text='Download', command=lambda: download_video(entry.get()), font=("Helvetica", 12), bg="blue", fg="white").grid(row=1, column=0, columnspan=2, pady=10)
master.mainloop()
