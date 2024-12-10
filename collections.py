# Collections are our vomplex data types
# different ways of storing data. 


# lists - ordered(indexed), mutable, collection of values
# [5(index poasition 0), 10(index position 1)....]   

# dictionaires - unordered(no index), mutable, collection of key:value pairs
# {"key1": "value1", key2: value1,.....} 

# tuples - ordered, immutable. () - or no barackets at all x = 1, 2, 3

# sets {} - unique values, unoredered and mutable.  


# Lists

# lists []

#colours = ["blue", "red", "yellow", "orange"]

#print(colours)

# direct access

#print(colours[0])
#print(colours[3])
#print(colours[-3])

# slicing

#print(colours[0:2]) # creates a sub list up to but not including the final number
#print(colours[1: ])

# altering a list with direct access

#food = ["pasta", "rice", "pizza", "bread"]

#food[0] = "apple"

#print(food)

# del

#del food[1]
#print(food)

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# methods 

# append

#my_fruits = ["apple", "pear", "orange", "kiwi"]

#my_fruits.append("blueberry")
#print(my_fruits)

# remove

#my_fruits.remove("apple")
#print(my_fruits)

# extend

#my_fruits.extend(["grapes", "melon"])
#print(my_fruits)

# insert 

#my_fruits.insert(0, "starfruit")
#print(my_fruits)

# sort

#my_fruits.sort()

#print(my_fruits)

#my_fruits.sort(key=len)
#print(my_fruits)

# join

#x = ", ".join(my_fruits)
#print(x)


# dictionaries
# keys need to be unique, vlaues can be anything.
# {}

#drinks = {"fizzy": ["sprite", "cola"], "still": "water", "juice": "orange", "alcoholic": "wine"}

#print(drinks)

# direct access

#print(drinks["fizzy"])

#drinks["non-alcoholic"] = "squash"

#print(drinks)

# methods

#print(drinks.values())
#print(drinks.keys())
#print(drinks.items())

# get
#print(drinks.get("still"))
#print(drinks.get("stillleee")) == None 
#print(drinks.get("stuilllelelelel", "not found"))

# update

#drinks.update({"sugery": "cola"})
#print(drinks)

# pop
#drinks.pop("still")
#print(drinks)

# exercie

# make a dictionary with 3 authors and multiple books per author.
# have an input that asks for an author name.
# Print a STRING of the books by that author. (not a list) use join. 
# opionally consider if the user inputs incorrect author name. 

# 1st solution

#books = {"author1": ["book1", "book2"], "author2": ["book3", "book4"]}

#x = input("enter an author name: ")

#print(", ".join(books[x]))

# 2nd solution 

#books = {"author1": ["book1", "book2"], "author2": ["book3", "book4"]}

#y = input("enter an author name: ")

#x = books.get(y, []) # None -- NOT AN ITERABLE

#print(", ".join(x) or "Author not found")


# tuples

#rectangle = 10, 5

#rectangle[0] = 15

# sets

#set1 = {1, 2, 3, 4, 5}
#set2 = {4, 5, 6, 7, 8}

#print(set1.union(set2))

#print(set1.intersection(set2))

#print(set1.symmetric_difference(set2))

#print(set1.difference(set2))


