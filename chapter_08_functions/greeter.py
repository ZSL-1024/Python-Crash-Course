# greeter.py
def greet_user():
    """Display a simple gretting."""
    print("Hello!")


greet_user()


# Passing Information to a Function
# Arguments and Parameters
# Parameter: a piece of information the function needs to do its job.
# An argument is a piece of information that is passed from a function call to a function.

def greet_user(username):
    """Display a simple gretting."""
    print("Hello, " + username.title() + "!")


greet_user('jesse')


# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
