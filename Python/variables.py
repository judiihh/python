###############################################################
#INTEGER
print(" ")
print("VARIABLE PARTE I")
print(" ")

myint = 7
print(myint)

###############################################################
#FLOATING POINT NUMBER
print(" ")
print("VARIABLE PARTE II")
print(" ")

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

###############################################################
#STRINGS
print(" ")
print("VARIABLE PARTE III")
print(" ")

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

###############################################################
#STRINGS USING APOSTROPHES
mystring = "Don't worry about apostrophes"
print(mystring)

###############################################################
#EXECUTING NUMBERS AND STRINGS
one = 1
two = 2
three = one + two
print(three)

###############################################################
#USING A 'SPACE' IN BETWEEN 2 VARIABLES
print(" ")
print("VARIABLE PARTE IV")
print(" ")

hello = "hello"
world = "world"
between = " "
helloworld = hello + between + world
print(helloworld)

###############################################################
#SIMULTANEOUS VARIABLES IN ONE LINE
print(" ")
print("VARIABLE PARTE V")
print(" ")

a, b = 3, 4
print(a, b)

cute, colors = "white", "pink"
print(cute, colors)

a, b, c, d, e = 1, 2, 3, 4, 5
print(a, b, c, d, e)

###############################################################
#EXERCISE
print(" ")
print("VARIABLE PARTE VI")
print(" ")

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

####################################################
print(" ")
print("VARIABLE PARTE VII")
print(" ")

prueba1 = "hola"
prueba2 = 20.5
prueba3 = 12

if isinstance(prueba1, str) and prueba1 == "hola":
        print("String: %s" % prueba1)
if isinstance(prueba2, float) and prueba2 == 20.5:
        print("Float: %f" % prueba2)
if isinstance(prueba3, int) and prueba3 == 12:
        print("Integer: %d" % prueba3)