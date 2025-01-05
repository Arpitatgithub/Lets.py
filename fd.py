total_amount=float(input("Enter amount: "))
interest_rate=float(input("Enter interest rate: "))

final_amount=total_amount*interest_rate/100
bank_balance=final_amount+total_amount
Interest_in_rupees=bank_balance-total_amount
year=float(input("Enter number of years: "))
print(f" Total available balance after interest of 1 year: {final_amount+total_amount}",f"\n Interest in percentage: {interest_rate}%",f" \n Interest in one year: {Interest_in_rupees}", f"\n Total amount after {year} years: {bank_balance+Interest_in_rupees}")