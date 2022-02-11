from __future__ import print_function


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


class Artist:
    """ basic class to store artist details

     Attributes:
         name (str): The name of the artist.
         albums (list[Album]): A list of the albums by this artist.
            The list includes only those albums in collection.

    Methods:
        add_album: Use to add a new album to the artist's album list
     """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
            If the album is already present, it will not get added again.
        """
        self.albums.append(album)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field, sep=" | ")

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

            if new_artist is not None:
                if new_album is not None:
                    new_artist.add_album(new_album)
                artist_list.append(new_artist)

        return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
