# Numberic
x = 12  #int
y = 25.25 #float 
z = 12j #complex
# print(type(x))
# print(type(y))
# print(type(z))
#  conversion
k = 25
j = 45.3j #can not convert
l = 10.65

# print(float(k))
# print(int(l))

import random
# print(random.randrange(1, 1000))


# Strings
s = """
    This is a multiline string.
    It has been enclosed in triple quotes.
    It allows for multi-line strings.
    And it supports escape characters like \n for newline.
"""
# print(s)

s1 = "Hello", "world"
# print(len(s1))

# loop
for i in "Apple":
    # print(i)
    
    txt = "The best things in life are free!"
# print("expensive" not in txt)


txt1 = "the coffee free for you guy"
if "the" in txt1:
    # print("Yes, 'The' is present")
    
# slicing string = to cut the string at the start index and end index
    a = "hello, world"
# print(a[2:5])
b = "tomorrow I and my girlfriend join the party."
# print(b[2:10])
c = "hello, world"
# print(c[-2:-2])

# modify string 
myLetter = "  HelLo, World  "
# print(myLetter.upper()) # convert all letters from lower to upper
# print(myLetter.lower()) # convert all letters from upper to lower
# print(myLetter.strip()) # to remove the whitespace from the beginning of the string to the end of the string
# print(myLetter.replace("o", "i")) # change the letter string to another string
# print(myLetter.split(",")) # change from string to substring

# String concatenation = to combine two variable in only one variable
x = "hello my bebe"
y = "you are my world"
z = x + " " + y
# print(z) # combine two variable in only one variable

# format string (f"{}")
age = 36 
txt = f" My name is John, I am {age}"
# print(txt) # combine numbers with strings

price = 59
tx = f"The price is {price:.2f} dollars for smart watch"
# print(tx) # combine numbers with strings

txts = f"The prices are {56*123} smart watch and air conditioner"
# print(txts) # combine numbers with strings

# Escape characters = To insert characters that are illegal in a string, use an escape character.
xt = "I love \"you\" bebe"
xt = "It\'s good"
xt = "I love you \fbebe"
xt = "\110\145\154\154\157\160\161"
# print(xt) 

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# # index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# # replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
