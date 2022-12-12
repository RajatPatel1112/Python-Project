#Color print
"""
1. Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends... 
   it's up to you how many and what kinds of things you pick. Keep it wacky!
2. Now construct your story - it can be about anything you want, but must use the variables you've created in step 1.
   Make sure to only work one paragraph at a time. Otherwise things could get a bit messy.

Take this sample code output/story as an example:

Welcome to your adventure simulator. 

I am going to ask you a bunch of questions and then create an epic story with you as the star!

What is your name?
What is your worst enemy’s name?
What is your superpower?
Where do you live?
What is your favorite food?

Hello {name}! Your ability to {superpower} will make sure you never have to look at {worst enemy’s name} again. 
Go eat {your favorite food} as you walk down the streets of {where you live} and use {superpower} for good and not evil!
"""




print("=== Your adventure Simulator ===")
print("""You'll be asked a bunch of questions then we'll make you up an amazing story with YOU as a star! 🤩""")
print("")
name = input("Your name: ")
enemy = input("Your worst enemy's name:")
superPower = input("Your super power: ")
print("")
print("Our story begings as our hero name approaches a doreboding castle...")
print("Suddenly a bolt of lightning striked the ground at the feet of", name)
print("""\033[31m'Our final battle begins!'\033[0mshouts the evil",enemy,"clearly missing the fact that",
name,"has the power of\033[35m",superPower,"\033[0mwhich means they'll win quite easily"""")
