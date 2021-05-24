# 8-13 ex_user_profile.py
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

my_profile = build_profile('shili', 'zhuang', 
							location='guangzhou', 
							phone=123123123, 
							gender='male')
print(my_profile)