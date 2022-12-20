#rock paper scissors game
"""
Day13 Challenge
Start with this code below to ensure that whenever you use input, each player cannot see what the other player typed in 😉:

from getpass import getpass as input

For this version, you have two players. Player 1 and Player 2.
You will need to create if statements (and probably nesting) to decide who has won, lost or if the game is a tie.
Make it fun and add emojis or epic comments as your players battle it out.
Keep it simple for you. Don't expect the user to type in the words rock, paper, scissors. Instead, encourage them to use R, P, or S. (Can you ensure the user can still input an option even if it is typed in wrong?)
"""







from getpass import getpass as input
print("E P I C 🪨 📃  ✂️ B A T T L E ")
print("Select your move (rock, paper or scissors)")
p1 = input("Player 1 > ")
p2 = input("Player 2 > ")
if p1 == "rock" or "paper"  or "scissor" and p2 == "rock" or "paper"  or "scissor":
  if p1 == "rock":
    if p2 == "paper":
      print(f"Player1's {p1} is smothered by Player2's {p2}!")
    elif p2 == "scissor":
      print(f"Player2's {p2} is smothered by Player1's {p1}!")
    else:
      print(f"Player1's {p1} and Player2's {p2}, so, it's a draw")
  elif p1 == "paper":
    if p2 == "scissors":
      print(f"Player1's {p1} is smothered by Player2's {p2}!")
    elif p2 == "rock":
      print(f"Player2's {p2} is smothered by Player1's {p1}!")
    else:
      print(f"Both, Player1 and Player2 choose {p1}, so, it's a draw")
  elif p1 == "scissors":
    if p2 == "rock":
      print(f"Player1's {p1} is smothered by Player2's {p2}!")
    elif p2 == "paper":
      print(f"Player2's {p2} is smothered by Player1's {p1}!")
    else:
      print(f"Both, Player1 and Player2 choose {p1}, so, it's a draw")
else:
  print("Enter Valid Move!")


