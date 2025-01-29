# Boolean Value it has two values (true and false)
# print("1",12 > 10)
# print("2", 10 == 9)
# print("3", 25 > 20)

a = 200
b = 150
if b > a:
    # print("b is greater than a")
# else:
    # print("a is greater than b")
    
    # using bool() function allows you to evaluate any value
    # print(bool("Hello"))
    # print(bool(15))
    
    x = "Hi bebe"
y = 20
# print(bool(x))
# print(bool(y))

class myclass():
    def _len_(self):
        return True
myobj = myclass()
# print(bool(myobj))
def myfunctions():
    return 5
if myfunctions():
    # print("YES")
# else:
    # print("NO")
# print(bool(myfunctions()))

# isinstance = used for checking data types of a built-in function
    z = 500
# print(isinstance(z, int))

# Python operator are used to perform operations on variables and values.

# *Python divides the operators in the following groups:

#  - Arithmetic operators used with numeric values to perform common mathematical operations:
    print(5 + 23)
    # + addition
    # - substraction
    # * multiplication
    # / division
    # % modulus
    # // floor division
    print(23 // 23)
    # ** exponentiation
    print(23 ** 23)
#  - Assignment operators are used to assign values to variables:
    # x = 5
    # x += 2
    # x -= 2
    # x *= 2
    # x /= 2
    # x %= 2
    # x //= 2
    # x **= 2
#  - Comparison operators are used to compare two values:
    # == equal
    #!= not equal
    # > greater than
    # < less than
    # >= greater than or equal
    # <= less than or equal
#  - Logical operators are used to combine conditional statements:
    # and true if both statements are true
    c = 5
    v = 10
    print("N1",c and v)
    # or true if one of the statements is true
    c = 5
    v = 10
    print("N2",c or v)
    # not (!=) both statements are true but reversed the result of returning false
    c = 5
    v = 10
    print("N3", c != v)
#  - Identity operators used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
    # is it's true if the both variables are the same object
    c = 10
    v = 10
    # v = 5
    print("I2", c is v)
    # is not it's true if the both variables are not the same object
    c = 10
    # v = 10
    v = 5
    print("I2", c is not v)
#  - Membership operators`are used to test if a sequence is presented in an object:
    # in (==) Returns True if a sequence with the specified value is present in the object
    c = 10
    v = 5
    print("i1", c == v)
    # not in (!=) Returns True if a sequence with the specified value is not present in the object
    c = 10
    v = 5
    print("i1", c != v)
#  - Bitwise operators are used to compare (binary) numbers:
    # & AND = Sets each bit to 1 if both bits are 1	    
    w = 2
    n = 10
    print("B1", w & n)
    # | OR = Sets each bit to 1 if one of two bits is 1	
    w = 2
    n = 10
    print("B2", w | n)
    # ^ XOR = Sets each bit to 1 if only one of two bits is 1	
    w = 2
    n = 10
    print("B3", w ^ n)
    # ~ NOT = Inverts all the bits	
    w = 2
    n = 10
    print("B4",  ~n)
    print("B5", ~w)

    # << left shift = Shift left by pushing zeros in from the right and let the leftmost bits fall off	
    w = 2
    n = 10
    print("B6", w << n)

    # >> right shift = Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	
    w = 2
    n = 10
    print("B7", w >> n)
    
    # Operator precedence describes the order in which operations are performed.

    print("P1",(12 + 3) - (10 + 3))
    print("P2",100 + 5 * 3)
    print("P3",5 + 4 - 7 + 3)
    s = 5
    s += 3
    print("P4",s)




    
