# 8-4 large_shirts.py
# shirts are large by default with a message that reads I love Python
def make_shirt(size='large', message='I love python.'):
	"""summarizing the size of the shirt and the message printed on it"""
	print("\nI am going to make a " + size + " t-shirt.")
	print('It will say: "' + message + '"')	

# default
make_shirt()
# keyword arguments
make_shirt(message='haha', size='medium')