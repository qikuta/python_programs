# Quentin Ikuta
# August 7, 2022
# This program takes input from user, anything from a-z, A-Z, or 0-9 --
# converts the input into ASCII code, then finally prints the original input and ASCII code.

# ask user for input
user_string = input("please enter anything a-z, A-Z, and/or 0-9:")

# iterate through each character and/or number, compare to dictionary of ASCII, pull the appropriate ASCII letter.
asciiDict = {i: chr(i) for i in range(128)}

keyList = list(asciiDict.keys())
valList = list(asciiDict.values())


def letter_to_ascii(user_string):
    indexlist = []
    for letter in user_string:
        letterindex = valList.index(letter)
        indexlist.append(letterindex)
    return indexlist


print(letter_to_ascii(user_string))
print(user_string)





