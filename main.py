"""
Name: Brian Wachira
Date started: 29/03/2025
"""
# TODO: Create your main program in this file, using the SongListApp class

from kivy.uix.button import Button
from songcollection import SongCollection
from kivy.lang import Builder
from kivy.app import App
from song import Song

#Color constrains
LEARNED_COLOR = (0.7, 0.7, 0.1, 1) 
UNLEARNED_COLOR = (0, 0.5, 0.7, 1)  

class SongListApp(App):
    def __init__(self):
        super().__init__()
        self.songs = SongCollection()
    
    def build(self):
        self.title = "Song List 2.0 By Brian Wachira"
        self.songs.load_songs("songs.json")
        self.root = Builder.load_file("app.kv")
        if self.root:
            self.update_status()
            self.display_songs()
        else:
            print("Error: Root widget is None")
        return self.root

    def on_stop(self):
        self.songs.save_songs("songs.json")
    
    def update_status(self):
        to_learn = self.songs.get_number_of_unlearned_songs()
        learned = self.songs.get_number_of_learned_songs()
        self.root.ids.status_label.text = f"To learn: {to_learn}  Learned: {learned}"
    
    '''Display the songs in buttons'''
    def display_songs(self):
        songs_box = self.root.ids.songs_box
        songs_box.clear_widgets()
        for song in self.songs.songs:
            button = Button(
                text=str(song),
                size_hint_y=None,
                height= 80,
                background_color=LEARNED_COLOR if song.is_learned else UNLEARNED_COLOR
            )
            button.bind(on_press=lambda btn, s=song: self.toggle_song_status(s))
            songs_box.add_widget(button)
    
    
    def toggle_song_status(self, song):
        if song.is_learned:
            song.mark_unlearned()
        else:
            song.mark_learned()
        self.update_status()
        self.display_songs()
    
    #sort and update. Before sorting temporarily change all to lower 
    def sort_songs(self, key):
        self.songs.sort(key.lower())
        self.display_songs()
    
    #In this function we'll add a new song and check the logics
    #ie, complete fields, year > 0 and Enter a valid number
    def add_song(self):
        title = self.root.ids.title_input.text.strip()
        artist = self.root.ids.artist_input.text.strip()
        year_text = self.root.ids.year_input.text.strip()
        
        if not title or not artist or not year_text:
            self.root.ids.message_label.text = "Complete all the fields"
            return
        
        try:
            year = int(year_text)
            if year <= 0:
                self.root.ids.message_label.text = "The year must be >0"
                return
        except ValueError:
            self.root.ids.message_label.text = "Enter a valid number"
            return
        
        new_song = Song(title, artist, year, False)
        self.songs.add_song(new_song)
        self.clear_inputs()
        self.update_status()
        self.display_songs()
        self.root.ids.message_label.text = f"Added {title} by {artist}"
    
    #Clear everything in the inputs
    def clear_inputs(self):
        """Clear the input fields and message label."""
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.message_label.text = ""


if __name__ == "__main__":
    SongListApp().run()