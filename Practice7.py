# fruits=("apple","banana","cherry","mango")
# index=0
# for i in fruits:
#           print(index,i)
#           index+=1

# for index,a in enumerate(fruits):
#           print(index,a)

# for index,i in enumerate(fruits,start=2):
#           print(index,i)

# Creating a dictionary from a list
 
# fruit_list=(i for i in enumerate(fruits))
# fruit_list=[index for index in enumerate(fruits)]
# fruit_dict={index:i for index,i in enumerate(fruits) }
# print(fruit_dict,"\n",fruit_list,"\n",fruits)

# import math
# import math as m
# from math import sqrt
# from math import sqrt,sum
# from math import*



# print(dir(math))
# result = m.sqrt(int(input("Enter any number ")))
# print(result)  
 
# import example

# def add(a,b):
#      return a+b

# x=int(input("Enter first number "))
# y=int(input("Enter second nnumber: "))
# print(f"the sum of {x} and {y} is: ",add(x,y))

# import os

# print(os.listdir())

# local and global variables
# def func():
#           y=5
#           print(y)

# func() 

# x=10
# def func():
#           print(x)
# func()      

# def func():
#           global x
#           x=200
#           print(x)
# func()  

# x=200
# def func():
#           global x
#           x=100
#           print(x)
         


# print(x) 

file=open("one","r")
content=file.read()
print(content)
file.close()



