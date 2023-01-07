#Multiplication Table
"""
Day20 Challenge
Prompt the user by asking for a multiplication table for the number of their choice.
Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question (psst...that's a hint).
If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.
At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.
Why not give users an emoji if they get all 10 math facts correct?
"""








print("Math Game!\n")

num = int(input("Name your multiples : "))
counter = 0
for i in range(1,11):
  print(i,"X",num,"=")
  ans = int(input(""))
  if ans==i*num:
    print("Great Work!👌\n")
    counter += 1
  else:
    print("Nope!🙅‍♂️ The answer was",i*num)

if counter == 10:
  print("Awesome,🙌 You got all answers correct 10/10")
else:
  print(f"You scored {counter} out of 10!")

