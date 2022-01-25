from jukebox_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please, choose your album (invalid choice terminates):\n")
    for index, value in enumerate(albums):
        title, artist, year, songs = value
        print(index + 1, title)
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song or put \"0\" to get back to albums list:\n")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        continue

    print("Playing {} by {}".format(title, albums[choice - 1][1]))
    print("_"*40)