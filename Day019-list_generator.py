#List Generator
"""
Day19 Challenge
Ask the user to list a starting number, ending number, and increment to use. 
Display an answer based on the users' answers (use the input command.)
"""








print("List Generator\n")
start = int(input("Start a : "))
end = int(input("End before : "))
inc = int(input("Increment between values : "))
for i in range(start,end+1,inc):
  print(i)
