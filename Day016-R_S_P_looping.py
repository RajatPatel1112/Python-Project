#Making R_S_P game loop from day13 
"""
Day16 Challenge
find your Rock, Paper, Scissors game from Day13 and add the code here before you start and build it as steps given below
. Use a loop to repeat the game multiple rounds.
. Keep score of player 1 and player 2.
. End the game when a player wins three rounds using break and exit.
. Use continue to restart the round until one player wins three rounds.
. Your last bit of code should be the results of which player won and what number of games each won.
"""







from getpass import getpass as input
print("E P I C 🪨 📃  ✂️ B A T T L E ")
round = 1
p1_score = 0
p2_score = 0
draw = 0
while True:
  print(f"Round {round}\n")
  print("Select your move (R, P or S)\n")
  p1 = input("Player 1 > ")
  p2 = input("Player 2 > ")
  if p1 == "R" or "P" or "S" and p2 == "R" or "P" or "S":
    if p1 == "R":
      if p2 == "P":
        print(f"Player1's {p1} is smothered by Player2's {p2}!\n")
        p2_score += 1
        
      elif p2 == "S":
        print(f"Player2's {p2} is smothered by Player1's {p1}!\n")
        p1_score += 1
        
      else:
        print(f"Player1's {p1} and Player2's {p2}, so, it's a draw\n")
        draw += 1
        
    elif p1 == "P":
      if p2 == "S":
        print(f"Player1's {p1} is smothered by Player2's {p2}!\n")
        p2_score += 1
        
      elif p2 == "R":
        print(f"Player2's {p2} is smothered by Player1's {p1}!\n")
        p1_score += 1
        
      else:
        print(f"Both, Player1 and Player2 choose {p1}, so, it's a draw\n")
        draw += 1
        
    elif p1 == "S":
      if p2 == "R":
        print(f"Player1's {p1} is smothered by Player2's {p2}!\n")
        p2_score += 1
        
      elif p2 == "P":
        print(f"Player2's {p2} is smothered by Player1's {p1}!\n")
        p1_score += 1
        
      else:
        print(f"Both, Player1 and Player2 choose {p1}, so, it's a draw\n") 
        draw += 1
  else:
    print("Enter Valid Move!")
    
  round += 1
  if p1_score == 3 or p2_score == 3:
    break
  elif draw == 3:
    print("You both had 3 times draw\n")
    if p1_score > p2_score:
      print(f"So player1 wins with score {p1_score}")
    elif p1_score < p2_score:
      print(f"So player2 wins with score {p2_score}")
    else:
      print("No one wins")
    break
  else:
    continue
print(f"Player1 Score : {p1_score} \nPlayer2 Score : {p2_score}")
