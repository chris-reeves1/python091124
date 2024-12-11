# loops - repeat blocks of code.
# saves time, avoid duplication. 
# 2 types - while and for

# while

# needs a condition to get started
# need a condition to stop
# continuously executes the block of code. 

#x = 0 
#while x < 101:
#    print(x)
#    x += 1

# break + continue

#i = 0

#while i < 6:
    #if i == 3:
     #   break
    #print(i)
    #i += 1 

#j = 0

#while j < 6:
  #  j += 1
 #   if j == 3:
#        continue (skip)
#    print(j)

#while True:
#    name = input("enter a name: ")

 #   if name == "quit":
  #      break
   # else:
    #    print(f"hello {name}")

# for loops
# for interating through a iterable. 

#my_fruits = ["apple", "pear", "orange", "kiwi"]

    # item   # iterable 
#for x in my_fruits:
#    print(x)

#l = 0
#while l < len(my_fruits):
 #   print(my_fruits[l])
  #  l += 1 


# range

#for a in range(5):
 #   print(a)

#for a in range(1, 4):
#    print(a)

#for a in range(1, 10, 2): # steps
    #print(a)


# Strings

#for letter in "hello":
#    print(letter)

#for word in "hello world".split():
   # print(word)

# List comprehension - making lists or changing lists

         #expression  #item   #iterable   
#result = [ x**2      for x in range(5)]
#print(result)

#result = []

#for x in range(5):
#    result.append(x**2)

#print(result)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

                        # expression # item # iterable #condition
#even_squared_numbers = [number**2 for number in numbers if number % 2 == 0]

#print(even_squared_numbers)

# dictionaries

#for i in {"still": "water"}:
 #   print(i)

#for i in {"fizzy": "cola"}.values():
 #   print(i)

#for i, y in {"drink": "water"}.items():
    #print(i, y)

# nested loops

#for i in range(1,3):
   # for j in range(1,4):
   #     print(i, "x", j, "=", i*j)

# exercise:

# write a loop that takes in 5 names as input and prints the name + is cool. 

# while loop
# for loop
# list comprehnsion
# optional - list comp 1 line of code only!! 

#counter = 0

#while counter < 5:
  #  name = input("enter a name: ")
 #   print(name + " is cool")
 #   counter += 1


#for x in range(5):
  #  name = input("enter a name: ")
  #  print(name + " is cool")


#names = [input("enter a name: ") for name in range(5)]

#for name in names:
#    print(f"{name} is coooooool")

# combined list comp



#inner list
#[input("enter name: ") for x in range(5)]
#outer list
#[print(f"{name} is cool") for name in iterable]

# list comp side affect

x = [print(f"{name} is cool") for name in [input("enter name: ") for x in range(5)]]

print(x)