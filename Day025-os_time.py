#Using os and time module
"""
Day25 Challenge
Use a function to create a title for a music player and
allow the user to select to play a song and use subroutine called 'play' when they select the song.
Give the user the option to exit the program.
The title should pop up and pause along with the menu options.
If the user chooses anything else, start again by clearing the screen.

use os module as:
os.system("clear")
to clear the screen

and time module as:
time.sleep(1) #write any number of seconds in bracket


Use tis sample code:
from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  Start taking user input and doing something with it
  input()
while True:
  # clear the screen 
  # Show the menu
  # take user's input
  # check whether you should call the play() subroutine depending on user's input
"""




from replit import audio
import os, time

def play():
  source = audio.play_file('cradles.mp3')
  source.paused = False
  title = input("Enter title : ")
  return title
x = play()
print(x)
while True:
  os.system("clear")
  time.sleep(1)
  print("Press 1 to play")
  print("Press 2 to Exit")
  print("Press anythig else to see the menu\n")

  choose = int(input("Choose any option : "))
  print("\n")
  if choose==1:
    play()
  elif choose==2:
    break
  else:
    continue    
  
  
