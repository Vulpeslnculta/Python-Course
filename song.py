class Song:
    """Class to represent a song
    
    Attributes:
        title       (str)
        artist      (Artist)
        duration    (int)
    
    """
    def __init__(self, title, artist, duration=0):

        self.title = title
        self.artist = artist
        self.duration = duration


help(Song.__doc__)

class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        album_name (str)
        year (int)
        artist (Artist)
        tracks (List[Song])

    Methods:
        addSong: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds a song to the track list:

        :param song: (Song)
        :param position: (Optional[int])
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)