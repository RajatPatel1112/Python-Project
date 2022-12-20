#More of if else program
"""
Day8 Challenge
Generation Name	    Starting Birth Year    	Ending Birth Year
Traditionalists	          1925	                 1946
Baby Boomers	            1947	                 1964
Generation X	            1965	                 1981
Millenials	              1982  	               1995
Generation Z	            1996	                 2015

Have a user type in the year they were born.
Use their answer to tell them the generation they are a part of.
Add emojis or a fun statement to go along with the answers if you like.
"""





print("Generation Identifier","\n")
year = int(input("Wnich year were you born? "))
if year >= 1883 and year <= 1900:
  print("Lost Generation")
elif year >= 1901 and year <= 1927:
  print("Greatest Generation")
elif year >= 1928 and year <= 1945:
  print("Silent Generation")
elif year >= 1946 and year <= 1964:
  print("Baby Boomers")
elif year >= 1965 and year <= 1980:
  print("Generation X")
elif year >= 1981 and year <= 1996:
  print("Millennials")
elif year >= 1997 and year <= 2012:
  print("Generation Z")
elif year >= 1965 and year <= 2022:
  print("Generation Alpha")
else:
  print("Plz enter year between 1883 to 2022")
