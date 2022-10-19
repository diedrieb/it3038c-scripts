import pygenius

artist = 'Drake'

album = 'Take Care'

print("Everything you need to know about the musical artist Drake!")

print(artists.getArtistBio(artist))

print("List of Drake's Albums" + artists.albumList(artist, arg))

print("The most popular song by Drake is" + artists.getPopularSongs(artist, arg))

print("Information about Drake's popular album Take Care is included here:" + artists.getAlbumData(artist, album))
