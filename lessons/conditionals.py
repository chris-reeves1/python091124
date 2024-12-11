# if elifs, elses
# allows for different pathways depending on certain conditions being met. 

#my_bool = False

#if my_bool:
#    print("my_bool is true")
#else:
#    print("my_bool if false")    


#is_admin = True
#is_verified = False
#on_holiday = False

#if is_admin or is_verified and not on_holiday:
#    print("ACCESS GRANTED")
#else:
#    print("Access not granted")

# elif

#temp = 20

#if temp >= 30:
#    print("its very hot")
#elif temp > 25:
#    print("pretty hot")
#elif temp > 10:
#    print("ok")
#elif temp == 0:
#    print("its freezing")
#else:
#    print("it bad or really bad")

# exercise:
# user to input a mark/grade
# if the mark is >= 85 print distinction
# if the mark is 65-84 pass
# otherwise fail
# just with ifs then with elifs

# multiple comparators

#deposit = 101
#password = "password1"

#if 0 < deposit < 100 and password == "password":
#    print(f"thanks for deposit of {deposit}")
#else:
#    print("failed to deposit")

# not

#if not 0 < deposit < 100 and password != "password":
#    print("failed to deposit")
#else:
#    print(f"thanks for deposit of {deposit}")

# in and not in

#name = "root123"

#if name in ("root", "admin", "user"):
#    print("invalid username")
#else: 
#    print("accepted")

#if name not in ("root", "admin", "user"):
#    print("accepted")
#else:
 #   print("invalid username")

# exercise:
# weight converter app
# user to input weight
# user to input if using Kgs of Lbs
# if statements to check for unit entered
# logic to convert weight (kgs to lbs or lbs to kgs)
# print out converted value
# optional- errot handling for lower/uppercase inputs
# very optional - error handling for numeric input. 

# 1st solution

#weight = float(input("enter weight: "))
#unit = input("enter K (kgs) or L (Lbs)")

#if unit.upper() == "K":
  #  converted = weight / 0.45
 #   print(f"converted weight is {converted}")
#elif unit.upper() == "L":
 #   converted  = weight * 0.45
#    print(f"converted weight is {converted}")
#else:
    #print("invalid choice!!!!!!")

# 2nd solution

#try:
#    result = 10/0
#except ValueError:
 #   print("A ValueError occured")
#except ZeroDivisionError:
#    print("Division by zero is not allowed") 
#except:
 #   print("an error has occured")
#except Exception as e:
#    print(f"an error occurd: {e}")
#finally:
#    print("clean up actions go here???")

# 2nd solution
#import sys
#while True:
    #try: 
   #     weight = float(input("enter weight: "))
  #      break
  #  except ValueError:
 #       print("invalid input, should be numeric")
        #sys.exit()

#while True:

   # unit = input("enter K (kgs) or L (Lbs)").upper()

    #if unit == "K":
     #   converted = weight / 0.45
     #   print(f"converted weight is {converted}")
    #    break
    #elif unit == "L":
    #    converted  = weight * 0.45
    #    print(f"converted weight is {converted}")
    #    break
   # else:
   #     print("invalid choice enter K or L !!!!!!!!!")


# highest number

#num = 30
#num1 = 20

#if num > num1:
 #   print(num)
#else: 
  #  print(num1)

# rewrite without using if statements or any in-built functions (no max!!)

#num = 50
#num1 = 40

#result = (num > num1) * num + (num <= num1) * num1
#print(result)

#result = num1 + (num - num1) * (num >= num1)
#print(result)