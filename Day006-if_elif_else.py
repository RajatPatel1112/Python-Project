#Use if-elif-else concept
"""
Day6 Challenge
Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
Write a specific personalized greeting for 3 different people.
Don't forget an else statement for everyone else who shouldn't be logging in.
"""






print("My Login System")
print("+++++++++++++++")
username = input("Username : ")
pswd = input("Password : ")
if username=="rajat" and pswd=="1112":
  print("Hello there Rajat, What a lovely accent you have, you could have charmed your way in here even without a password")
  print("Have a great day.")
  
elif username=="meet" and pswd=="2003":
  print("Hello there Meet, What a lovely accent you have, you could have charmed your way in here even without a password")
  print("Have a great day.")
  
elif username=="priyanshu" and pswd=="6789":
  print("Hello there Priyanshu, What a lovely accent you have, you could have charmed your way in here even without a password")
  print("Have a great day.")
  
else:
  print("Your username or password is wrong.")
