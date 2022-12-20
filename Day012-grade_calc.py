#Simple grade calculator
"""
Day12 Challenge
1. You are going to ask the user to type in the name of a test, maximum score they could receive, 
and how many points they received. For example, your test could be called "Python Skills" and 
the maximum score is 50 points and the user receives 30 points out of 50 possible points.
2. Figure out the percentage the user received and round to 2 decimal places.
3. Use if/elif statements to show users the letter grade they received.
4. At the end, the user should see the letter grade they received and the percentage correct.
5. Add in emojis to celebrate their good grade or different colors depending on what you think is a good or bad final grade.

You can grade system given below
Letter Grade	Percentage
A+	          90-100
A	            80-89
B	            70-79
C	            60-69
D	            50-59
E             40-49
F             0-40
"""









print("Exam Grade Calculator\n")
exam = input("Name of exam : ")
print("\n")
max_score = float(input("Max. Possible Score: "))
print("\n")
stdnt_score = float(input("Your score: "))
print("\n")
percent = round((stdnt_score/max_score)*100,2)
if percent>=90 and percent<=100:
  print(f"You got {percent}% which is A+")
elif percent>=80 and percent<=89:
  print(f"You got {percent}% which is A")
elif percent>=70 and percent<=79:
  print(f"You got {percent}% which is B")
elif percent>=60 and percent<=69:
  print(f"You got {percent}% which is C")
elif percent>=50 and percent<=59:
  print(f"You got {percent}% which is D")
elif percent>=40 and percent<=49:
  print(f"You got {percent}% which is E")
else:
  print(f"You got {percent}% which is F(Failed)")
  
