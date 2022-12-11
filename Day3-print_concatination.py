#concatenation in print statement
"""
Create these as a variable:
A type of food,
A type of plant,
A method of cooking,
A word to describe burned food,
A household item

Output a nice looking Recipe page that *concatenates* a dish in this format:
cooking food with burned plant on a bed of item
"""



food = input("Name a food -> ")
plant = input("Name a type of plant -> ")
method = input("Name a method of cooking -> ")
desc_food = input("What word describes burned food? -> ")
diy = input("Name a DIY item -> ")
print(" ")
print("MENU")
print(method,food,"with",desc_food,plant,"on a bed of",diy)
