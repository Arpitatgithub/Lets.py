# If else statements

# a=10
# b=20
# if (a<b):
#           print("a is smaller then b")
# else:
#         print("a is bigger then b")

# num=input()
# if (int(num)<5):
#           print("num is less then 5")
# elif (int(num)==5):
#               print("num is equal to 5")
# else:
#       print("num is greater then 5")

# try:
#     num=int(input("Enter any numeric value: \n"))
#     an1="Number is Negative"
#     an2="Number is in between 1 and 10"
#     an3="Number is in between 11 and 20"
#     an4="Number is greater then 20"
#     an5="Number is equal to 0"
#     if (num<0):
#               print(an1.center(50,"*"))
#     elif(num >0):
#             if(num>0 and num<=10):
#                     print(an2.center(50,"*"))
#             elif(num>10 and num<=20):
#                     print(an3.center(50,"*"))
#             else:
#                     print(an4.center(50,"*"))   
#     else:
#             print(an5.center(50,"*"))
# except ValueError:
#     print("Enter a valid numeric number ")

# x = 4
# match x:
#     case 0:
#         print("x is zero")
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
#     # Empty case with if-condition
#     case _ if x < 10:
#         print("x is < 10")
#     # default case(will only be matched if the above cases were not matched)
#     # so it is basically just an else:
#     case _:
#         print(x)

# try:
#     num=int(input("Enter any valid number: \n"))

#     match num:
#               case 0:
#                 print("The number is zero")
#               case a if (a>0 and a<=10):
#                 print("The number is between 1 and 10")
#               case b if (b>10 and b<=20):
#                 print("The number is in between 11 and 20")
#               case c if (c>20):
#                 print("The number is greater then 20")
#               case _:
#                 print("The number is negative")
# except ValueError:
#   print("Enter a valid numeric number") 
         


                                