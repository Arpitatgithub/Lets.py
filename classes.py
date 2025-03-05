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