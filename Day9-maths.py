"""
Day9 Challenge
Ask the user for the total bill amount.
Ask what % of tip they will leave to be added to the bill total.
Figure out how to get the total bill with tip then add that to original amount.
Ask the user how many people are splitting the bill and divide by the total.
"""





print("Tip Calculator","\n")
spend = float(input("How much did you spend? "))
print("\n")
per = int(input("What percent do you want to tip? "))
print("\n")
div = int(input("How many people in your group? "))
print("\n")

total_amount = spend + ((per/spend)*100)
each_person_cost = total_amount/div
print("You each owe $",end="")
print(each_person_cost)
