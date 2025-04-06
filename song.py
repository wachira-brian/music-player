# This class fully represents an object song 
class Song:    
    def __init__(self, title="", artist="", year=0, is_learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned
    
    def __str__(self):
        status = "learned" if self.is_learned else "unlearned"
        return f"{self.title} by {self.artist} ({self.year}) ({status})"
    
    def mark_learned(self):
        self.is_learned = True
    
    def mark_unlearned(self):
        self.is_learned = False