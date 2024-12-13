# modules

# libraries - such as the standard library. Can contain multiple packages and modules.
# packages - directory of modules
# module - just python files. 

#import math 

#number = 10

#answer = math.sqrt(number)

#print(answer)

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
#    print(random_pi())

#from math import ceil, pi, floor
#from random import randint

#def random_pi():
#    return ceil(randint(1,10) * pi)

#for i in range(5):
#    print(random_pi())


# files

# - logs
# - storing data/ retrieval of data
# - configs
# - running scripts

# focus on txt.files:

# read mode - ("r") - default mode - used for reading from the file.
# write mode - ("w") - opens the file for writing, creates if doesnt exist. 
# append ("a") - append to the end - will create if doesnt exist. 

# eg:

#file = open("example.txt", "mode")
#-------------
#files.close()


# reading from file
# read() read the entire file as a string
# readline() - reads a line and moves on to the next
# readlines() - reads all lines - puts them in a list.
# seek() - go to beinging or s specific line. 

# writing:
# write() - writing a string to the file
# writelines() writng a list to the file. 

#file = open("lines.txt", "r")

#lines = file.readlines()

#print(lines)

#file.close()

#file = open("lines-new.txt", "w")

#for n in range(1,11):
  #  newline = "this is new line" + " " + str(n) + "\n"
 #   file.write(newline)

#file.close()

file = open("lines-new.txt", "r")

outfile = ""

for line in range(1, 11):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("lines-new.txt", "w")

file.write(outfile)
file.close()

#with open("lines.txt", "r") as file:
#    code. . . .. .. . .
#    files.write() ...... .

















