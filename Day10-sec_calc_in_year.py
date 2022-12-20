# seconds calculator in a year
"""
You can multiply a bunch of numbers to figure out how many seconds are in a year.
Use input and if statements to add the extra day for leap year.
Make the computer do all the hard work and math for you. You do the thinking beforehand.
"""





sec = 1 
min = sec*60
hour = min*60
day = 24*hour
one_year = 365*day
leap_year = one_year+day

year = int(input("Enter year : "))
if (year >= 1600) and (year <= 100000):
  if ((year%4 == 0) and (year%100 != 0)) or ((year % 400 == 0) and (year % 100 == 0)):
    print(f"{year} is a leap year so it has {leap_year} sec")
  else:
    print(f"{year} has {one_year} sec")
else:
  print("Enter valid year.")
