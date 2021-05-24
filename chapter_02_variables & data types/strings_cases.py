#	Changing Case in a String with Methods

name = "abaaba waibibabu"
print(name.title())

print(name.upper())
print(name.lower())

#	Combining or Concatenating Strings

first_name = "aba"
last_name = "waibi"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

#	Storing the entire message in a variable

message = "Hello, " + full_name.title() + "!"
print(message)

#	Adding Whitespace to Strings with Tabs or Newlines
#	\n means newline, \t means tab

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#	Stripping Whitespace

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())