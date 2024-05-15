"""Task A"""


def playlists(songs: list[set[str]]) -> list[str]:
    result = songs[0]
    for song_list in songs:
        result = result.intersection(song_list)
    return sorted(list(result))


def playlists_input(n=int(input())):
    songs = []
    for i in range(n):
        k = int(input())
        song_list = set(input().split())
        songs.append(song_list)
    result = playlists(songs)
    length = len(result)
    result = ' '.join(result)
    print(length)
    print(result)


playlists_input()
