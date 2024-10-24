import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from lyrics_extractor import SongLyrics

# Create the main window
window = Tk()
window.geometry('600x600')
window.title('Sandeep Music Lyrics Extractor')

# Frame for border and header
border_color = Frame(window, background="red")
border_color.pack(padx=40, pady=40)

# Header label
head = Label(border_color, text="Enter the song you want Lyrics for", font=('Calibri', 15))
head.pack(padx=1, pady=1)

# Variables to store song name and result
song = tk.StringVar()  # For storing entered song name

# Function to fetch and display lyrics
def get_lyrics():
    song_name = song.get()  # Get the song name entered by the user
    api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine_id = "aa2313d6c88d1bf22"
    extract_lyrics = SongLyrics(api_key, engine_id)  # Initialize the lyrics extractor
    song_lyrics = extract_lyrics.get_lyrics(song_name)  # Fetch lyrics
    lyrics_box.config(state=NORMAL)  # Enable editing of the text box
    lyrics_box.delete(1.0, END)  # Clear previous content
    lyrics_box.insert(INSERT, song_lyrics['lyrics'])  # Insert new lyrics
    lyrics_box.config(state=DISABLED)  # Disable editing of the text box

# Entry for song name
Entry(window, textvariable=song).pack(pady=10)

# Scrollable text widget to display the lyrics
lyrics_box = scrolledtext.ScrolledText(window, wrap=WORD, width=50, height=20, bg="light grey", font=('Calibri', 12))
lyrics_box.pack(pady=10)
lyrics_box.config(state=DISABLED)  # Initially, make the text box read-only

# Create GO button to trigger the lyrics fetch
Button(window, text="GO", command=get_lyrics, width=30, fg="red").pack(pady=10)

# Start the Tkinter main loop
window.mainloop()