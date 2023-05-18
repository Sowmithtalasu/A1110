import numpy as np
import random
import soundfile as sf
from tkinter import Tk, filedialog
import tkinter as tk
import pygame
import os


os.environ['SDL_VIDEODRIVER'] = 'x11'

def next_song():
    play_next_song()
    update_current_song_label()

def get_music_files(folder_path):
    music_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):
            music_files.append(os.path.join(folder_path, file))
    return music_files


def quit_player():
    pygame.mixer.music.stop()
    window.quit()
        
def play_next_song():
    global song_index
    song_index = (song_index + 1) % len(playlist)
    pygame.mixer.music.load(playlist[song_index])
    pygame.mixer.music.play()

def choose_music_folder():
    Tk().withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path
    
def shuffle_playlist():
    global playlist, shuffled_playlist, song_index
    shuffled_playlist = playlist.copy()
    np.random.shuffle(shuffled_playlist)
    song_index = 0
    pygame.mixer.music.load(shuffled_playlist[song_index])
    pygame.mixer.music.play()

def update_current_song_label():
    current_song_label.config(text=f"playing : {os.path.basename(playlist[current_song_index])}")


pygame.init()


music_folder = choose_music_folder()


playlist = get_music_files(music_folder)


current_song_index = 0
shuffle_playlist()


window = tk.Tk()
window.title("Song Playlist")
window.geometry("400x200")


current_song_label = tk.Label(window, text="Current Song: ")
current_song_label.pack()


quit_button = tk.Button(window, text="Quit", command=quit_player)
quit_button.pack()

next_song_button = tk.Button(window, text="Next ", command=next_song)
next_song_button.pack()


update_current_song_label()


pygame.mixer.init()
pygame.mixer.music.load(playlist[current_song_index])
pygame.mixer.music.play()


window.mainloop()


pygame.quit()
