# variables - a reference(a name), a selection of memory (memory location).
# protected location. 

#x = 20
#person_one_age = 20

# naming convention: should be descriptive, follow a style guide, be consistant.
# Dont start with a number, a capital, no keywords pls. 

#1age = 10 # not allowed
#Age = 10 # class names!
#AGE = 10 # constants - we do not want the value to change
#print # avoid keywords


#PascalCase - class names/file names
#camelCase - vars/functs/methods
#snake_case - var/functs/methods

# we will come back to this. #
#a = 100
#b = 100

#print(a is b)

#def test():
   # a = 100
   # b = 100
   # c = 1000
  #  d = 1000
 #   print(a is b, c is d)

#test()

#def t1():
#    c = int(str(200))
#    return c
#def t2():
#    d = int(str(200))
#    return d

#print(t1() is t2())

#data types

# int = number
# string = char, text, paragraphs 
# floats = decimal numbers
# bolleans = true or flase, 0 or 1, something or nothing. 

# scope

#global_variable = "accessible everywhere"

#def my_function():
  #  local_variable = "accessible only inside the function"
  #  print(local_variable)
 #   print(global_variable)

#my_function()
#print(local_variable)

# in built functions

#print("hello")
#input("enter a number: ")

#import sys

#with open("output.txt", "w") as file:
 #   sys.stdout = file
 #   print("Go to the file!!!")

#sys.stdout = sys.__stdout__
#print("hello")

# escape chars

# \ to escape and take the next symbol as its literal meaning
# \\ backslash, \t tab, \n newline, \u unicode, \U extended unicode. 

#print("Person1: \tHey how are you?\nPerson2: \tim good thanks! \U0001f604")

# string concatenation:

#name = input("enter an age")
#age = int(input("Enter your age: "))

#message = "your name is {}, your age is {}".format(name, age)
#print(message)

#print("your name is " + name)
#print("your name is ", name, "your age is ", age) 

#print(f"your name is {name}, your age is {age}")

# BODMAS

# brackets
# order of
# division
# multiplication
# addition
# subtraction

# + - / *
# floor division 10//3 = 3
# modulo % 10%3 = 1

# String methods

#print("HELLO WORLD".lower())
#print("hello world".upper())

#print("heelo world".count("o", 3, -3))

#print("hello world world world".replace("world", "class", 2))

#print("he#llo#wor#ld".split("#")) #string to list


