"""

A possible collection of classes which can be used to
represent a music collection (for example, inside a music player),
focusing on how they would be related by composition.
You should include classes for songs, artists, albums and playlists.
For simplicity you can assume that any song or album
has a single “artist” value (which could represent more than one
person), but you should include compilation albums
(which contain songs by a selection of different artists).
The “artist”
of a compilation album can be a special value like
“Various Artists”. You can also assume that each
song is associated with
a single album, but that multiple copies of the
same song (which are included in different albums) can exist.
Write a simple implementation of this model which
clearly shows how the different classes are composed.
Write some
example code to show how you would use your classes 
to create an album and add all its songs to a playlist.
Class Album
should have a method to add track, class Artist should
have methods to add album and add song, class Playlist should also
have a method to add song.

"""


class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration}m)"


class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []

    def add_track(self, song):
        self.tracks.append(song)

    def __str__(self):
        return f"Album: {self.title} by {self.artist}"


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Artist: {self.name}"


class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist: {self.title}"



artist = Artist("Various Artists")
album = Album("Road Trip Mix", artist.name)

s1 = Song("Highway Star", "Deep Purple", album.title, 6)
s2 = Song("On the Road Again", "Willie Nelson", album.title, 3)
s3 = Song("Drive", "Incubus", album.title, 4)

for song in (s1, s2, s3):
    album.add_track(song)
    artist.add_song(song)

artist.add_album(album)

playlist = Playlist("Weekend Drive")
for track in album.tracks:
    playlist.add_song(track)

print(album)
print(playlist)
for idx, track in enumerate(playlist.songs, 1):
    print(f"{idx}. {track}")