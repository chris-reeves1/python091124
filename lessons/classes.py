# classes is part of OOP (object orientated programming)
# 4 principles of OOP: 
# - abstraction: i want to implement but not see the code.  
# - polymorphism: different ways of implementing methods(fuctions)
# - encapsulation: privacy  
# - inheritance: inhering from parent class.


# - class - a blueprint 
# - object - an instance of a class
# - multiple objects of the same type. 

#class Example:
  #  name = "chris"

 #   def speak(self):
 #       print("hello")

#person = Example()
#person1 = Example()
#person.name = "john"
#print(person.name)
#print(person1.name)

#class Students:
#    pass

#student1 = Students()
#student2 = Students()

#student1.name = "john"
#student1.age = 10
#student2.group = "group1"

#class Students:
 #   def __init__(self, first, last, age): # init method
 #       self.first = first #initialising the object with these values
 #       self.last = last # self refers to the object itself
 #       self.age = age # self maps the class data to the object. 

#student1 = Students("john", "smith", 10)
#student2 = Students("katy", "smith", 12)

#print(student1.age, student2.first)

#cl#ass Students:

    #full = "" # object inherits but not in dictionary until changes. 

  #  def __init__(self, first, last, age): 
 #       self.first = first 
 #       self.last = last 
 #       self.age = age
 #       self.full = first +  " " + last

#student1 = Students("john", "smith", 10)
#student2 = Students("katy", "smith", 12)

#print(student1.full, student2.first)

#class Students:
   # def __init__(self, first, last, age): 
  #          self.first = first 
  #          self.last = last 
  #          self.age = age
            #self.full = first +  " " + last

 #   def fullName(self):
 #       return self.first + " " + self.last

#student1 = Students("john", "smith", 10)
#student2 = Students("katy", "smith", 12)

#print(student1.age, student2.first)
#print(student1.fullName())
#print(Students.fullName(student2))


#class Students:
    #def __init__(self, first, last, age): 
      #      self.first = first 
     #       self.last = last 
    #        self.age = age
            #self.full = first +  " " + last

   # def fullName(self):
   #     return self.first + " " + self.last

  #  def change_age(self):
 #       self.age = self.age + 1  

#student1 = Students("john", "smith", 10)
#student2 = Students("katy", "smith", 12)

#student1.change_age()
#print(student1.age, student2.age)


#class Students:

    #age_increase_amount = 25

   # def __init__(self, first, last, age): 
   #         self.first = first 
   #         self.last = last 
   #         self.age = age
            #self.full = first +  " " + last

  #  def fullName(self):
  #      return self.first + " " + self.last

 #   def change_age(self):
 #       self.age = self.age + self.age_increase_amount  

#student1 = Students("john", "smith", 10)
#student2 = Students("katy", "smith", 12)

#student1.change_age()
#print(student1.age, student2.age)#

#print(student1.age_increase_amount)

# __dict__

#print(student1.__dict__)
#print(student2.__dict__)
#print(Students.__dict__)

#student1.age_increase_amount = 20
#student1.change_age()

#print(student1.age)
#print(student1.__dict__)
#print(student2.__dict__)

# non self class variable

#class Students:

    #age_increase_amount = 25
   # __num_of_students = 0

  #  def __init__(self, first, last, age): 
      #      self.first = first 
     #       self.last = last 
     #       self.age = age
            #self.full = first +  " " + 
            
    #        Students.__num_of_students += 1

   # def fullName(self):
   #     return self.first + " " + self.last

  #  def change_age(self):
  #      self.age = self.age + self.age_increase_amount 

  #  @classmethod
 #   def getNumofStudents(cls):
 #           return cls.__num_of_students 

#student1 = Students("john", "smith", 10)
#student2 = Students("katy", "smith", 12)
#print(Students._Students__num_of_students)
#print(Students.getNumofStudents())

# inheritace

#class Animal:
   # def __init__(self, name, species):
  #      self.name = name
  #      self.species = species

 #   def eat(self):
 #       print(f"{self.name} is eating")

#class Cat(Animal):
   # def __init__(self, name, species, breed):
   #     super().__init__(name, species)
  #      self.breed = breed

 #   def meow(self):
 #       print("meow")

#my_cat = Cat("w", "y", "z")

#my_cat.meow()
#my_cat.eat()


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} - {self.species} - {self.__class__.__name__}"

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    def __str__(self):
        return super().__str__() + f" {self.breed}"

my_cat = Cat("w", "y", "z")

my_cat.meow()
my_cat.eat()
print(my_cat)