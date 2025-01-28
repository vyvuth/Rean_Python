# Variable is the container for storing the value that we asigned
# Casting 
x = str(3) #x = will be "3"
y= int(3)#y = will be 3
z = float(3.0) #z = will be "3"
# print(x)
# print( y)
# print(z)

# to defin the type function
x = 5 # type = initger function
y = 2.56 # type = float function
z = "50" # type = string function
# print(type(z))

# Case-sensitive
a = 4
A = "Bally"
# A will not  overwrite a
# overwrite  = giving variable one to other variables 
# print(A*a)

#Variable names
myLove = "I love you!"
_varMain = 23
my2 = " crush on you! "
# print(myLove)
# print(_varMain)
# print(my2)

# Variable Name 
#Camel case
myLoveYou = "I love you!"
# Pasel case
myLoveYou2 = "I love you!"
# Snake case
My_Love_You = "I love you!"

# Assign value to multiple variables
# meaning: python allow you assign value to multiple variables in one line
x, y, z= "Apple", "Banana", "Orange"
# print(z)
x, y,z = 21, 22, 23
# print(x+z/y+z-x*y)

# x, y, z = "Apples"
# print(x)

fruit = ["grapes", "banana", "orange", "pineapple"]
a, b, c, d = fruit
# print(a)
# print(b)
# print(c)
# print(d)

# food = [
#     {"pizza"},
#     {"burger"},
#     {"pasta"}
# ]
food = {"pizza", "burger", "pasta"}
h, i, j = food
# print(h)
# print(i)
# print(j)

# output variables
x = 5
y = 5
# print(x+y)
# print("hello", "hello")

# global variables
x = "you"
y = 256
def myFeel():
    global z
    z = 1200
    y = 300
    print("I love " + x)
    print(100 + y)

myFeel()
print(5000 - z)

x = "awsome"
def felMyFeel():
    x = "fantastic"
felMyFeel()
print(x)

a = 'Hello'
b = 'World'
print(a + b)
