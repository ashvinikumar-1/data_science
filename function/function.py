# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations'+'!!!'
    # Print shout_word
    print(shout_word)


# Define shout with the parameter, word
def shout_param(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)


# Define shout with the parameter, word
def shout_ret(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return

    return shout_word


# Pass 'congratulations' to shout: yell
yell = shout_ret('congratulations')

# Print yell
print(yell)

# Call shout with the string 'congratulations'
shout_param('congratulations')

# Call shout
shout()

