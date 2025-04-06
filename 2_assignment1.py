"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to

"""
Name: Brian Wachira
Date started: 04/03/2025
"""

import json
from songcollection import SongCollection
from song import Song

FILENAME = "songs.json"

def load_songs():
    """Load songs from a JSON file into a SongCollection."""
    songs = SongCollection()
    try:
        songs.load_songs(FILENAME)
        print(f"{len(songs.songs)} songs loaded.")
    except FileNotFoundError:
        print("No songs file found. Starting with an empty list.")
    return songs

def display_songs(songs):
    """Display all songs sorted by year, then title."""
    if not songs.songs:
        print("No songs in list.")
        return

    sorted_songs = sorted(songs.songs, key=lambda x: (x.year, x.title))
    unlearned_count = sum(1 for song in songs.songs if not song.is_learned)
    learned_count = len(songs.songs) - unlearned_count

    for i, song in enumerate(sorted_songs, 1):
        mark = "*" if not song.is_learned else " "
        print(f"{i}. {mark} {song.title} - {song.artist} ({song.year})")

    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")

def add_song(songs):
    """Add a new song to the collection."""
    print("Enter details for a new song.")

    while True:
        title = input("Title: ").strip()
        if title:
            break
        print("Input cannot be blank.")

    while True:
        artist = input("Artist: ").strip()
        if artist:
            break
        print("Input cannot be blank.")

    while True:
        try:
            year = int(input("Year: ").strip())
            if year > 0:
                break
            print("Number must be > 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")

    new_song = Song(title, artist, year, False)
    songs.add_song(new_song)
    print(f"{title} by {artist} ({year}) added to song list.")

def complete_song(songs):
    """Mark a song as learned."""
    unlearned_songs = [song for song in songs.songs if not song.is_learned]

    if not unlearned_songs:
        print("No more songs to learn!")
        return

    display_songs(songs)

    while True:
        try:
            choice = int(input("Enter the number of a song to mark as learned: ")) - 1
            if 0 <= choice < len(songs.songs):
                if not songs.songs[choice].is_learned:
                    songs.songs[choice].is_learned = True
                    print(f"{songs.songs[choice].title} by {songs.songs[choice].artist} learned.")
                else:
                    print(f"You have already learned {songs.songs[choice].title}.")
                break
            print("Invalid song number.")
        except ValueError:
            print("Invalid input; enter a number.")

def save_songs(songs):
    """Save songs to the JSON file."""
    songs.save_songs(FILENAME)
    print(f"{len(songs.songs)} songs saved to {FILENAME}")

def main():
    """Main program function."""
    print("Song List 2.0 - by Yue Zhou")
    songs = load_songs()

    while True:
        print("\nMenu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ").strip().lower()

        if choice == "d":
            display_songs(songs)
        elif choice == "a":
            add_song(songs)
        elif choice == "c":
            complete_song(songs)
        elif choice == "q":
            save_songs(songs)
            print("Make some music!")
            break
        else:
            print("Invalid menu choice.")

if __name__ == '__main__':
    main()