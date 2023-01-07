#Creating a function and concept of recursion
"""
Day22 Challenge
Create a subroutine with both a username and password.
Create a loop to prompt the user again and again until they put in the correct login information.
"""














print("LOGIN SYSTEM\n")
def login():
  uname = "rajat"
  pswd = "1234"
  username = input("Username : ")
  password = input("Password : ")
  if username == uname and password == pswd :
    print("Login Successfull")
  else:
    print("Try Again, username or password seems incorrect.\n")
    login()

login()
