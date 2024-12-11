# a function either returns a value or performs a task
# repeatability

#def greet(name): # defines the params of the funct. Takes args. 
#    print(f"hello {name}")

#greet("chris")

# default args:

#def greet1(first_name, last_name, age=10): #positional args
#    print(f"{first_name} {last_name} is {age}")

#greet1("chris", "reeves", 15)

# return

#def greeter(name):
#    return f"hello {name}"


#x = greeter("name")
#print(x)
#print(greeter("name"))

# *args
# if we dont know how many args wil be passed through
# receives a tuple of args

#def fruit_list(*fruits):
  #  print("the list of fruits is:")
 #   for fruit in fruits:
 #       print(fruit)

#fruit_list("orange", "apple", "pear")

#def make_pizza(size, *toppings):
  #  print(f"order for {size}-inch pizza with the following toppings:")
 #   for topping in toppings:
 #       print(topping)

#make_pizza(12, "peppers", "mushrooms")

# kwargs 
# order doesnt matter if using keyword args
# send args as key=value

#def fruit_list(fruit1, fruit2, fruit3):
#    print(f"fruit 1 is {fruit1}")
#    print(f"fruit 2 is {fruit2}")
#    print(f"fruit 3 is {fruit3}")

#fruit_list(fruit3="apple", fruit1="pear", fruit2="kiwi")

# **kwargs
# If we dont know how many keyword args will be passed through

#def fav_food(**food):
#    print(f"fav food is", food["desert"], "not", food["dairy"])

#fav_food(desert="ice-cream", dairy="milk", fruit="apple")

# combined

#def combine(*args, **kwargs):
#    print("args ", args)
#    print("kwags", kwargs)

#combine(2, c=3, a=5, b=10)

# /
# introduced in python 3.8
# before / is positional arg only and is enforced
# after can be keywords(nothing is enforced)

#def example(a, b, /, *, c, d):
   # print(f"a = {a}, b = {b}, c = {c}, d = {d}")

#example("a", "b", "c", d="d")

#def maths_function(a, b, /, operation="add", *, decimal_place=4):
   # if operation == "add":
   #      result = a + b
   # elif operation == "subtract":
  #      result = a - b
  #  else: 
 #       raise ValueError("invalid operation")
 #   return round(result, decimal_place)
    

#print(maths_function(10, 5, "subtract"))
#print(maths_function(10.24656, 5.32656, decimal_place=2))
#print(maths_function(10, 5, 5))

# recurrsion

#def factorial(n):
   # if n == 1:
   #     return 1
  #  else:
 #       return n * factorial(n - 1)

#print(factorial(5))

# lambda fucntions
# short unnamed functions, calculate a single expression. 

# lambda argument: expression (iterable)
 
#add_lambda = lambda x, y: x + y 
#print(add_lambda(2, 4))

#numbers = [1, 2, 3, 4]

#squared = map(lambda x: x**2, numbers)

#print(list(squared))

# higher order functions
# either takes in a fucntion as an arg or returns a function
# wrapper

# def square(x):
#    return x * x

#def apply_fucntion(func, value):
#    return func(value)

#print(apply_fucntion(square, 5))








