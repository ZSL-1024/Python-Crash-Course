guests = ['victor', 'william', 'zimo']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it.")

# william can't join dinner, so let's invite hugo
del guests[1]
guests.insert(1, 'hugo')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

print("\nHello everyone, I just found a bigger dinner table, so now more space is available.\n")

# Use insert() to add one new guest to the beginning of your list.

guests.insert(0, 'tina')

# Use insert() to add one new guest to the middle of your list.

guests.insert(2, 'mike')

# Use append() to add one new guest to the end of your list.

guests.append('tenny')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# Shrinking guest list, using pop() to remove four guests.

print("\nSorry I just found out that my new dinner table won’t arrive in time for the dinner, so I have space for only two guests.")

popped_guest = guests.pop()
print("\nSorry, I can't invite " + popped_guest.title() + " to dinner.")

popped_guest = guests.pop()
print("\nSorry, I can't invite " + popped_guest.title() + " to dinner.")

popped_guest = guests.pop()
print("\nSorry, I can't invite " + popped_guest.title() + " to dinner.")

popped_guest = guests.pop()
print("\nSorry, I can't invite " + popped_guest.title() + " to dinner.")

name = guests[0].title()
print("\n" + name + ", you are still invited.")

name = guests[1].title()
print("\n" + name + ", you are still invited.")

del guests[0]
del guests[0]
print(guests)