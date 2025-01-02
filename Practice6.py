# def factorial(n):
#           if n == 0:
#                   return 1
#           else:
#                   return n * factorial(n-1)
# print(factorial(9))      
 
            
 # Modify recursion limit

# num={1,2,3,4}
# # num.add(5)


# num.update([4,5,6,7])
# print(num)

# set={1,4,3}
# set.pop()
# print(set)

# a={1,2,3,4}
# b={3,4,5,6}

# print(a|b)
# print(a.union(b)) #union of two sets

# print(a&b)
# print(a.intersection(b)) #intersection of two sets

# print(a-b)
# print(a.difference(b)) #difference of two sets

# print(a^b)
# print(a.symmetric_difference(b)) #symmetric difference of two sets

# math_st={"arpit","aman","ankush","abishek","nishant"}
# science_st={"arpit","abishek","shreya","nishant"}
# computer_st={"aman","ankush","shreya","rohit"}
# print("all students" , math_st|science_st|computer_st )
# print("students in math and science" , math_st & science_st)
# print("students in math and computer" , math_st & computer_st)
# print("students in science and computer" , science_st & computer_st)

# Python Dictionaries

# stu={"name":"Arpit","Age":20}
# stu["contact"]=9469280356
# stu["Age"]=21
# print(stu)

# stu = dict(name="Arpit",age=20, gender="Male", salary=89000)
# print(stu.pop("age"))
# del stu["gender"]
# print(stu)

# for key,value in stu.items():
#           print(key,":",value)

# grades={}
# while True:
#           actions=input("'add','view ','quit'")
#           if actions=='add':
#                   name= input("Enter student name :")
#                   grade=input("Enter grade :")
#                   grades[name]=grade
#           elif actions=='view':
#                   for key,value in grades.items():
#                           print(key,":",value)
#           elif actions=='quit' :
#                   break
#           else:
#                   print("invalid input")
# print(grades)                                         

