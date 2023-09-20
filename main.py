import tkinter
import customtkinter
from pytube import YouTube

def starDownload():
    try:
        youtubelink = link.get() # catching the url
        youtubeObject = YouTube(youtubelink, on_progress_callback= on_progress)
        video = youtubeObject.streams.get_lowest_resolution()
        title.configure(text= youtubeObject.title, text_color="white") # adding the title video 
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Downloaded")
    except:
        finishlabel.configure(text="Download Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compleation = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compleation))
    progress.config(text= per + '%')
    progress.update()

    # update progress bar

    progressBar.set(float(percentage_of_compleation) / 100)


# System Settings 

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI elements

title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx = 10, pady = 10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width= 350, height= 40, textvariable= url_var)
link.pack()

# Finish Downloading

finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress Bar

progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressBar = customtkinter.CTkProgressBar(app, width= 400)
progressBar.set(0)
progressBar.pack(padx= 10, pady= 10)

# Download button

download = customtkinter.CTkButton(app, text="Download", command= starDownload)
download.pack(padx = 10, pady= 10)

# Run App

app.mainloop()