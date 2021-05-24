# 8-3 t-shirt.py 

def make_shirt(size, message):
	"""summarizing the size of the shirt and the message printed on it"""
	print("\nI am going to make a " + size + " t-shirt.")
	print('It will say: "' + message + '"')	

# positional arguments
make_shirt('medium', 'hello world!')
# keyword arguments
make_shirt(message='haha', size='large')