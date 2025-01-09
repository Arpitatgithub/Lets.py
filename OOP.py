# class data:
#           name="Arpit"
#           age=20
# data()          

# class Person:
#     # Constructor method (initializer)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Method to display information
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# # Creating an object
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)

# # Accessing methods
# person1.display()
# person2.display()

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

# dog1 = Dog("Buddy,", "Golden Retriever")
# print(dog1.name, dog1.breed)



# class animal:
#     def __init__ (self,name,breed):
#         self.name = name
#         self.breed = breed

# dog1= animal("Simba","Indian")
# print(dog1.name,dog1.breed)


# class report:
#           def __init__(self,marks,grades):
#                   self.marks=marks
#                   self.grades=grades

# Final_grades=report(72,"B+")
# print(Final_grades.marks,Final_grades.grades)

# class index:
#           def __init__(self,Sno,Content):
#                   self.sno=Sno
#                   self.content=Content

# Index_1=index(92,"Daffodills")
# print(Index_1.sno,Index_1.content)
          


#                             Pillars of OOP


# Encapsulation


# class BankAccount:
#           def __init__(self,acc_no,balance):
#                   self.__acc_no=acc_no
#                   self.__balance=balance
#           def get_balance(self):
#                   return self.get_balance
#           def deposit(self,amount):
#                   if amount >0:
#                           self.__balance +=amount
#                           print(f"{amount} deposited. New balance is: {self.__balance}")

# account=BankAccount("1233445",100000)
# print("balance", account.get_balance)
# account.deposit(5000)


                                   
# Inheritance


# Base Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Derived Class
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Creating objects
dog = Dog()
cat = Cat()

dog.speak()  # Inherited from Animal class
dog.bark()

cat.speak()  # Inherited from Animal class
cat.meow()

                  



















































































































































































