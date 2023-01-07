# Loan Calculator
"""
Day18 Challenge
create a loan calculator that shows how much money you owe for a loan of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.
This means each year the amount of money you owe will increase 5%.
Figure out how much you owe altogether for 10 years?
Use a for loop and one or two lines of looped code to determine the answer.
"""









print("Loan Calculator\n")
loan = float(input("Enter the amount : "))
intr = float(input("Enter the interest rate : "))
year = int(input("Enter the number years : "))
loanx = loan
for i in range(1, year+1):
    x = float(loanx + (intr / 100) * loanx)
    print(f"Year {i} is {x}")
    loanx = x
interest = x - loan
print(f"You paid {interest} in interest")
