import os
import pygame
import tkinter as tk
from tkinter import filedialog, Listbox, messagebox, Scale
import random

# Initialize Pygame mixer
pygame.mixer.init()

# Main Music Player class
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Music Player")
        self.root.geometry("500x500")
        self.playlist = []  # List to store playlist
        self.current_song_index = None
        self.is_paused = False
        self.is_looping = False
        self.is_shuffling = False

        # Create GUI elements
        self.label = tk.Label(self.root, text="Music Player", font=("Arial", 20))
        self.label.pack(pady=10)

        self.playlist_box = Listbox(self.root, bg="black", fg="white", width=60, height=15)
        self.playlist_box.pack(pady=20)

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(self.root, text="Remove Song", command=self.remove_song)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.resume_button = tk.Button(self.root, text="Resume", command=self.resume_song)
        self.resume_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_song)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_song)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.volume_slider = Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(70)  # Default volume
        self.volume_slider.pack(pady=10)

        self.shuffle_button = tk.Button(self.root, text="Shuffle", command=self.toggle_shuffle)
        self.shuffle_button.pack(side=tk.LEFT, padx=5)

        self.loop_button = tk.Button(self.root, text="Loop", command=self.toggle_loop)
        self.loop_button.pack(side=tk.LEFT, padx=5)

    # Add a song to the playlist
    def add_song(self):
        song = filedialog.askopenfilename(initialdir=".", title="Select a Song",
                                          filetypes=(("MP3 Files", "*.mp3"),))
        if song:
            song = os.path.abspath(song)
            self.playlist.append(song)
            self.playlist_box.insert(tk.END, os.path.basename(song))

    # Remove the selected song from the playlist
    def remove_song(self):
        try:
            selected_song_index = self.playlist_box.curselection()[0]
            self.playlist_box.delete(selected_song_index)
            self.playlist.pop(selected_song_index)
        except IndexError:
            messagebox.showerror("Error", "No song selected")

    # Play the selected song
    def play_song(self):
        try:
            selected_song_index = self.playlist_box.curselection()[0]
            self.current_song_index = selected_song_index
            song_to_play = self.playlist[self.current_song_index]
            pygame.mixer.music.load(song_to_play)
            pygame.mixer.music.play(loops=0)
            self.label.config(text=f"Playing: {os.path.basename(song_to_play)}")
        except IndexError:
            messagebox.showerror("Error", "No song selected")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Pause the song
    def pause_song(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True

    # Resume the song
    def resume_song(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    # Stop the song
    def stop_song(self):
        pygame.mixer.music.stop()
        self.label.config(text="Music Player")
        self.is_paused = False

    # Play the next song in the playlist
    def next_song(self):
        if self.is_shuffling:
            self.current_song_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)

        self.playlist_box.selection_clear(0, tk.END)
        self.playlist_box.selection_set(self.current_song_index)
        self.play_song()

    # Play the previous song in the playlist
    def prev_song(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.playlist)

        self.playlist_box.selection_clear(0, tk.END)
        self.playlist_box.selection_set(self.current_song_index)
        self.play_song()

    # Set volume based on the slider value
    def set_volume(self, val):
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)

    # Toggle shuffle mode
    def toggle_shuffle(self):
        self.is_shuffling = not self.is_shuffling
        if self.is_shuffling:
            self.shuffle_button.config(text="Shuffle On")
        else:
            self.shuffle_button.config(text="Shuffle")

    # Toggle loop mode
    def toggle_loop(self):
        self.is_looping = not self.is_looping
        if self.is_looping:
            self.loop_button.config(text="Loop On")
            pygame.mixer.music.play(loops=-1)  # Loop infinitely
        else:
            self.loop_button.config(text="Loop")
            pygame.mixer.music.play(loops=0)  # No loop

# Run the music player
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
