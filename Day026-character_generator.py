"""
Day26 Challenge
Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:
(((6-sided-roll * 12-sided-roll)/2)+10)
Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:
(((6-sided-roll * 12-sided-roll)/2)+12)
Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
Wrap it in a loop so the user has the option to create another character.

Let code output be like:

⚔️Character Builder⚔️

Name Your Legend:
Sheila the Almighty

Character Type (Human, Elf, Wiard, Orc):
Human

Sheila the Almighty
HEALTH: 40
STRENGTH: 26

May your name go down in Legend...
"""








import random,os,time
print("⚔️Character Builder⚔️\n")
def char_gen():
  global name
  name = input("Name your Legend:\n")
  char_type = input("Character Type(Human, Elf, Wizard, Orc, imp):\n")
  if char_type == "Human" or char_type == "Elf" or char_type == "Wizard" or char_type == "Orc" or char_type == "imp":
    pass
  else:
    print("Invalid character.")
  return name
print("\n"+char_gen())

def health():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,12)
  total_health = (((roll1*roll2)/2)+10)
  return total_health
print("HEALTH:",health())

def strength():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,12)
  total_strength = (((roll1*roll2)/2)+12)
  return total_strength
print("STRENGTH: ",strength())

print("May your name go down in Legend...\n")

while True:
  again = input("Again? ")
  if again == "yes":
    time.sleep(1)
    os.system("clear")
    print("\n"+char_gen())
    health()
    print("HEALTH:",health())
    strength()
    print("STRENGTH: ",strength())
    print("May your name go down in Legend...\n")
  elif again == "no":
    break
  else:
    print("Invalid input.")









