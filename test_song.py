"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert default_song.is_learned is False

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    # TODO: Write tests to show this initialisation works
    print(initial_song)  # Check __str__() output
    assert initial_song.title == "My Happiness"
    assert initial_song.artist == "Powderfinger"
    assert initial_song.year == 1996
    assert initial_song.is_learned is True

    # TODO: Add more tests, as appropriate, for each method
    # Test changing learned status
    print("\nTesting mark as learned/unlearned:")
    initial_song.is_learned = False
    assert initial_song.is_learned is False
    print(f"Updated song status: {initial_song}")

    initial_song.is_learned = True
    assert initial_song.is_learned is True
    print(f"Updated song status: {initial_song}")

run_tests()