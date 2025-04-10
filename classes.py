# class Student:
#           name="Ayush"
#           age=19
#           classs=11

# a= Student()
# a.name="Arpit"
# print(a.name)



# class Student:
#           name="Ayush"
#           age=19
#           classs=11
#           def info(self):
#                   print(f"{self.name} is {self.age} years old")

# a= Student()
# b= Student()
# c= Student()
# d= Student()

# a.name="Arpit"
# a.age=12

# b.name="Simran"
# b.age=20

# c.name="Muskan"
# c.age=18

# a.info()
# b.info()
# c.info()

# class BankAccount:
#           def __init__(self, Acc_num, Balance=9000):
#                   self.Acc_num=Acc_num
#                   self.Balance=Balance
#           def deposit(self, Amount):
#                   self.Balance += Amount
#                   print(f"Deposited: {Amount}. New Balance: {self.Balance}")
#           def withdrawl(self, Amount):
#                   if Amount >= self.Balance :
#                           print("Insuffecient Funds!")
#                   else:
#                           self.Balance -= Amount
#                           print(f"Withdrawl Amount: {Amount}. New Balance: {self.Balance}")
#           def get_balance(self):
#                   return self.balance                     
# Acc1=BankAccount(3150)
# Acc1.withdrawl(1000) 
# Acc1.deposit(1000)    
# 

# class car:
#           def __init__(self,brand,model,mileage):
#                   self.brand=brand
#                   self.model=model
#                   self.mileage=mileage
#           def fuel_needed(self,distance):
#                   fuel = distance/self.mileage
#                   return f"Fuel needed for {distance} Km is {fuel} Litres"
#           #         return f"{fuel}"

# first=car("Audi","Q7",15) 
# print(first.fuel_needed(150))
 
# class rect:
#           def __init__(self, length, width):
#                   self.length=length
#                   self.width=width
#           def area(self):
#                   area=self.length*self.width
#                   return area
#           def perimeter(self):
#                   Peri= 2*(self.length + self.width)
#                   return Peri

# R1=rect(4,6)
# print(R1.area(),",",R1.perimeter())           

class Book:
          def __init__(self,title, author, price):
                  self.title=title
                  self.author=author
                  self.price=price
          def apply_discount(self,percent):
                  discount_amount = (percent / 100) * self.price
                  self.price -= discount_amount
                  return f"{self.price}"
price=int(input("Enter price: "))
discount_amount=int(input("Enter Discount Percentage: "))
book1=Book("50 Shades", "Peter Parker", price)
print(book1.apply_discount(discount_amount))                  

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # Public
#         self.balance = balance  # Public

# acc = BankAccount("12345", 1000)
# print(acc.balance)  # ✅ 1000 (Can access directly)

# acc.balance = -500  # ❌ Allowed, but incorrect data!
# print(acc.balance)  # ❌ -500 (Wrong balance!)
















