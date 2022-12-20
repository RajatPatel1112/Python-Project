# while True: //infinite loop
"""
Day15 Challenge
Create a "Name the Lyrics" game. Write your favorite song lyrics with a word or two missing. 
The user has to figure out the correct song lyric in as few attempts as possible.
Also let the user know how many attempts did he took to guess correctly.
"""







print("Fill in the blanks Lyrics!")
print("(type in the blank lyrics, see if you're as cool as me )\n")
counter=0
while True:
  fill = input("Never going to ________ you up\n")
  counter += 1
  if fill == "give":
    break
print(f"Well done, it took you {counter} attempts!")
