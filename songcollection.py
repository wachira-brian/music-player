import json
from song import Song

class SongCollection:    
    def __init__(self): #Initializing an empty list of songs
        self.songs = []
    
    def __str__(self):
        return "\n".join(str(song) for song in self.songs) if self.songs else "No songs in collection."
    

    def add_song(self, song):
        self.songs.append(song)
    
    def get_number_of_unlearned_songs(self):
        return sum(1 for song in self.songs if not song.is_learned)
    
    def get_number_of_learned_songs(self):
        return sum(1 for song in self.songs if song.is_learned)
    
    def load_songs(self, filename):
        try:
            with open(filename, 'r') as file:
                songs_data = json.load(file)
                self.songs = [Song(song["title"], song["artist"], song["year"], song["is_learned"])
                              for song in songs_data]
        except FileNotFoundError:
            self.songs = []  #If file doesn't exist, start with an empty list
    
    def save_songs(self, filename):
        songs_data = [{"title": song.title, "artist": song.artist, "year": song.year, "is_learned": song.is_learned}
                      for song in self.songs]
        with open(filename, 'w') as file:
            json.dump(songs_data, file, indent=4)
    
    def sort(self, key):
        self.songs.sort(key=lambda song: (getattr(song, key), song.title))
