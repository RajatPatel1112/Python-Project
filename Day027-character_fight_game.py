"""
. Add return functions to your character's health and strength statuses from Day 27's project.
. Generate two different characters and store their data (health and strength stats, character type, name, etc.).
. Use a while True loop to simulate those two characters battling.
. Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
. The winner of that round (the one who rolled the higher number) will give damage to the other character by doing 
  the following:
. Find the difference between the strength of both opponents and add one.
. Take that amount away from the loser's health.
. At the end of each round, check the stats of each character to ensure neither of them have died yet.
. When one character dies (they run out of health), declare a winner of the battle!
. To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") 
  to ensure the screen clears between battles.


OUTPUT sample:
⚔️Character Builder⚔️

Name your Legend:
Reyna
Character Type(Human, Elf, Wizard, Orc, imp):
imp

Reyna
HEALTH: 14
STRENGTH:  22

Who are they battling?

Name your Legend:
Jett
Character Type(Human, Elf, Wizard, Orc, imp):
Orc

Jett
HEALTH: 43
STRENGTH:  22
 
⚔️Battle Time⚔️
** CLEAR SCREEN**

Round 1
The battle Begins!

Reyna wins the first blow
Jett takes a hit, with 8 damage

Reyna
HEALTH: 14

Jett
HEALTH: 35

And they're both standing for the next round!
** CLEAR SCREEN**
 
⚔️Battle Time⚔️

Round 2
The battle Begins!

Reyna wins the first blow
Jett takes a hit, with 8 damage

Reyna
HEALTH: 14

Jett
HEALTH: 27

And they're both standing for the next round!
** CLEAR SCREEN**
 
⚔️Battle Time⚔️

Round 3
The battle Begins!

Jett wins the first blow
Reyna takes a hit, with 5 damage

Reyna
HEALTH: 9

Jett
HEALTH: 27

And they're both standing for the next round!
** CLEAR SCREEN** 
 
⚔️Battle Time⚔️

Round 4
The battle Begins!

Reyna wins the first blow
Jett takes a hit, with 5 damage

Reyna
HEALTH: 9

Jett
HEALTH: 22

And they're both standing for the next round!
** CLEAR SCREEN**

⚔️Battle Time⚔️

Round 5
The battle Begins!

Reyna wins the first blow
Jett takes a hit, with 4 damage

Reyna
HEALTH: 9

Jett
HEALTH: 18

And they're both standing for the next round!
** CLEAR SCREEN**

⚔️Battle Time⚔️

Round 6
The battle Begins!

Jett wins the first blow
Reyna takes a hit, with 8 damage

Reyna
HEALTH: 1

Jett
HEALTH: 18

And they're both standing for the next round!
 ** CLEAR SCREEN**
 
⚔️Battle Time⚔️

Round 7
The battle Begins!

Reyna wins the first blow
Jett takes a hit, with 4 damage

Reyna
HEALTH: 1

Jett
HEALTH: 14

And they're both standing for the next round!
** CLEAR SCREEN**

⚔️Battle Time⚔️

Round 8
The battle Begins!

Reyna wins the first blow
Jett takes a hit, with 3 damage

Reyna
HEALTH: 1

Jett
HEALTH: 11

And they're both standing for the next round!
** CLEAR SCREEN**

⚔️Battle Time⚔️

Round 9
The battle Begins!

Reyna wins the first blow
Jett takes a hit, with 7 damage

Reyna
HEALTH: 1

Jett
HEALTH: 4

And they're both standing for the next round!
** CLEAR SCREEN**

⚔️Battle Time⚔️

Round 10
The battle Begins!

Jett wins the first blow
Reyna takes a hit, with 5 damage

Reyna
HEALTH: -4

Jett
HEALTH: 4

And they're both standing for the next round!
** CLEAR SCREEN**

Jett destroyed Reyna in 10 rounds
"""








import random,os,time
print("⚔️Character Builder⚔️\n")

def char_gen1():
  global char1_name
  char1_name = input("Name your Legend:\n")
  char_type = input("Character Type(Human, Elf, Wizard, Orc, imp):\n")
  if char_type == "Human" or char_type == "Elf" or char_type == "Wizard" or char_type == "Orc" or char_type == "imp":
    pass
  else:
    print("Invalid character.")
  return char1_name
char1 = char_gen1()
print("\n"+ char1)

def char1_health():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,12)
  total_health = int(((roll1*roll2)/2)+10)
  return total_health
c1_health = char1_health()
print("HEALTH:", c1_health)

def char1_strength():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,12)
  total_strength = int(((roll1*roll2)/2)+12)
  return total_strength
c1_strength = char1_strength()
print("STRENGTH: ", c1_strength)

print("\nWho are they battling?\n")

def char_gen2():
  global char2_name
  char2_name = input("Name your Legend:\n")
  char_type = input("Character Type(Human, Elf, Wizard, Orc, imp):\n")
  if char_type == "Human" or char_type == "Elf" or char_type == "Wizard" or char_type == "Orc" or char_type == "imp":
    pass
  else:
    print("Invalid character.")
  return char2_name
char2 = char_gen2()
print("\n"+ char2)

def char2_health():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,12)
  total_health = int(((roll1*roll2)/2)+10)
  return total_health
c2_health = char2_health()
print("HEALTH:", c2_health)

def char2_strength():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,12)
  total_strength = int(((roll1*roll2)/2)+12)
  return total_strength
c2_strength = char2_strength()
print("STRENGTH: ", c2_strength)

os.system("clear")

counter = 1
while True:  
  print("⚔️Battle Time⚔️\n")
  print(f"Round {counter}")
  print("The battle Begins!\n")
  char1_roll = random.randint(1,8)
  char2_roll = random.randint(1,8)
  if char1_roll > char2_roll:
      c2_health = c2_health - char1_roll
      print(f"{char1_name} wins the first blow")
      print(f"{char2_name} takes a hit, with {char1_roll} damage\n")
    
      print(f"{char1_name}")
      print(f"HEALTH: {c1_health}\n")
    
      print(f"{char2_name}")
      print(f"HEALTH: {c2_health}\n")
  
      print("And they're both standing for the next round!")
    
    
  elif char2_roll > char1_roll:
    c1_health = c1_health - char2_roll
    print(f"{char2_name} wins the first blow")
    print(f"{char1_name} takes a hit, with {char2_roll} damage\n")
  
    print(f"{char1_name}")
    print(f"HEALTH: {c1_health}\n")
  
    print(f"{char2_name}")
    print(f"HEALTH: {c2_health}\n")

    print("And they're both standing for the next round!")

  else:
    c1_health = c1_health - char2_roll
    c2_health = c2_health - char1_roll
    print(f"{char1_name} and {char2_name} takes equal damage of {char1_roll}")
    
  
    print(f"{char1_name}")
    print(f"HEALTH: {c1_health}\n")
  
    print(f"{char2_name}")
    print(f"HEALTH: {c2_health}\n")

    print("And they're both standing for the next round!")

  if c1_health < 0 and c1_health < c2_health:
    os.system("clear")
    print(f"{char2_name} destroyed {char1_name} in {counter} rounds")
    break
  elif c2_health < 0 and c2_health < c1_health:
    os.system("clear")
    print(f"{char1_name} destroyed {char2_name} in {counter} rounds")
    break
  else:
    pass
    
  counter += 1 
  time.sleep(5)
  os.system("clear")
