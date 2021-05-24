# 8-7
def make_album(artist, title, tracks=''):
	"""Build a dictionary containing information about an album."""
	album_dict = {
		'artist': artist.title(),
		'title': title.title(),
		}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

album = make_album('orange ocean', 'tears in ocean')
print(album)

album = make_album('Cigarettes after sex', 'Cigarettes after sex')
print(album)

album = make_album('sunset rollercoaster', 'bossa nova', tracks=8)
print(album)

album = make_album('sunset rollercoaster', 'bossa nova', '8')
print(album)