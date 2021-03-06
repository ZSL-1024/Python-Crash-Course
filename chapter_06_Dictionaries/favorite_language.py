favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
 }

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + ".")

# A List in a Dictionary

# favorite_languages = {
# 	'jen': ['python', 'ruby'],
# 	'sarah': ['c'],
# 	'edward': ['ruby', 'go'],
# 	'phil': ['python', 'haskell'],
# 	}

# for name, languages in favorite_languages.items():
# 	print("\n" + name.title() + "'s favorite languages are:")
# 	for language in languages:
# 		print("\t" + language.title())

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
	print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " + 
			favorite_languages[name].title() + "!\n")

if 'erin' not in favorite_languages.keys():
	print("Erin, take the poll.\n")

# Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# Without repetition
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())