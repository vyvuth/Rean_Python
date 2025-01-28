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
print(txt) # combine numbers with strings

price = 59
tx = f"The price is {price:.2f} dollars for smart watch"
print(tx) # combine numbers with strings

txts = f"The prices are {56*123} smart watch and air conditioner"
print(txts) # combine numbers with strings

