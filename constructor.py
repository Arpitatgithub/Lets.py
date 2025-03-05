# class Student:
#           def __init__ (self,name,age):
#                   self.name=name
#                   self.age=age
#           def info(self):
#                   print(f"{self.name} is {self.age} years old")

# a=Student("Arpit",12)
# b=Student("Aayush",10)

# a.info()
# b.info()

class school:
          def __init__(self,classes,students,staff):
                  self.classes=classes  #attributes
                  self.students=students
                  self.staff=staff
          def info(self):
                  print(f"{self.classes} classes, {self.students} students and {self.staff} members")            #method

playway=school(12,350,42)
playway.info()                   