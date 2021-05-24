# 8-8
def make_album(artist, title, tracks=''):
	"""Build a dictionary containing information about an album."""
	album_dict = {
		'artist': artist.title(),
		'title': title.title(),
		}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

title_prompt = "\nWhat album are you thinking of?"
artist_prompt = "who's the artist?"

# Let the user know how to quit.
print("(enter 'q' at any time to quit)")
while True:
	
	album_title = input(title_prompt)
	if title == 'q':
		break
	
	artist_name = input(artist_prompt)
	if artist == 'q':
		break

	album = make_album(artist_name, album_title)
	print(album)

print("\nThanks for responding!")