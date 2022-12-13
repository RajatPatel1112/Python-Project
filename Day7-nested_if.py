#creating nested if_elif_else
"""
Day7 Challenge
Create a program that asks what someone is interested in and includes
nested if statements to ask annoying follow-up questions to see if 
someone is the real deal!
Make sure you include multiple if/elif statements and nested if statements too!

Let ouput be like:
What's your favourite anime? {input}

Oh really?! Name me any of the character? {input}

You got that by pure chance. Okay then, what is his job on the ship?{input}

hmph! What was his first bounty then? {input}

Nice, You are a true fan of one piece
"""





print("Fake Fan Finder 👀")
print("-------------------")
anime = input("What's your favourite anime? ")
if anime=="one piece":
  print("\n")
  char = input("Oh really?! Name me any of the character? ")
  if char=="luffy":
    role = input("You got that by pure chance. Okay then, what is his job on the ship?")
    if role == "captain":
      bounty = input("hmph! What was his first bounty then?")
      if bounty=="50Million":
        print("Nice, You are a true fan of one piece")
      else:
        print("See! You are a FAKE One Piece Fan ")
    else:
      print("See! You are a FAKE One Piece Fan")
      
  elif char=="zoro":
    role = input("You got that by pure chance. Okay then, what is his job on the ship?")
    if role == "swordsman":
      bounty = input("hmph! What was his first bounty then?")
      if bounty=="30Million":
        print("Nice, You are a true fan of one piece")
      else:
        print("See! You are a FAKE One Piece Fan ")
    else:
      print("See! You are a FAKE One Piece Fan")

if anime=="naruto":
  print("\n")
  char = input("Oh really?! Name me any of the character? ")
  if char=="naruto":
    goal = input("You got that by pure chance. Okay then, what is his goal to be?")
    if goal == "hokage":
      food = input("hmph! What is his favourite food?")
      if food=="ramen":
        print("Nice, You are a true fan of naruto")
      else:
        print("See! You are a FAKE naruto Fan ")
    else:
      print("See! You are a FAKE naruto Fan")
      
  elif char=="sasuke":
    goal = input("You got that by pure chance. Okay then, Whom he wanna kill so desperately?")
    if goal == "itachi":
      clan = input("hmph! What is name of clan he belong to?")
      if clan=="uchiha":
        print("Nice, You are a true fan of naruto")
      else:
        print("See! You are a FAKE naruto Fan ")
    else:
      print("See! You are a FAKE naruto Fan")
  
  else:
    print(f"See! You are a FAKE Fan of {anime}")
