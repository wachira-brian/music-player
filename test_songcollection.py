"""(Incomplete) Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection


def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    assert song_collection.songs  # assuming file is non-empty, non-empty list is considered True

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    # Test sorting songs
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)
    # TODO: Add more sorting tests
    print("Test sorting - by title:")
    song_collection.sort("title")
    print(song_collection)
    
    print("Test sorting - by artist:")
    song_collection.sort("artist")
    print(song_collection)
    
    print("Test sorting - by learned status:")
    song_collection.sort("is_learned")
    print(song_collection)

    # TODO: Test saving songs (check file manually to see results)
    print("Test saving songs:")
    song_collection.save_songs('test_songs.json')
    print("Check test_songs.json manually to verify the output.")

    # TODO: Add more tests, as appropriate, for each method
    # Test marking a song as learned
    print("Test marking a song as learned:")
    song_collection.songs[0].mark_learned()
    assert song_collection.songs[0].is_learned is True
    print(song_collection.songs[0])
    
    # Test marking a song as unlearned
    print("Test marking a song as unlearned:")
    song_collection.songs[0].mark_unlearned()
    assert song_collection.songs[0].is_learned is False
    print(song_collection.songs[0])
    


run_tests()