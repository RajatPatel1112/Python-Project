#Lists
"""
Day14 Challenge
Ask for a animal name from a given list
animal : cow,cat,dog,sheep,lion,goat,frog,bird,birds,sparrow,pig,donkey
print what sound does that animal make and ask if he/she wants to play again and continue until user asks for not to play
""" 






print("Here is the list of animals we got:")
print("cow,cat,dog,sheep,lion,goat,frog,bird,birds,sparrow,pig,donkey","\n")
exit_or_no = ""
while exit_or_no!="yes":
  ani = input("Which animal do you want? ")
  ani_list={"cow":"moo","cat":"meow","dog":"woof","pig":"oink","donkey":"hee-haw","sheep":"baa","goat":"baa","bird":"chirp","birds":"chirp","sparrow":"chirp","frog":"ribbit","lion":"roar"}
  if ani in ani_list:
    print(f"A {ani} goes {ani_list.get(ani)}")
  else:
    print("Plz ask for animals from above list")
  exit_or_no = input("Do you want to exit? ")
  
  
