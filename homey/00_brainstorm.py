#!/usr/bin/env python
categ = ["Reptiles", "Vegetables", "Brands", "Technology", "Colors", "Restaurants", "Countries",  "Books", "Shops", "Plants", "Emotions", "School Subjects", "Cartoons", "Clothes", "Holidays", "Fruits", "Holidays"]

#run = raw_input("Start? > ")
#mins = 0
# Only run if the user types in "start"
#if run == "start":
    # Loop until we reach 20 minutes running
  #  while mins != 20:
       # print( ">>>>>>>>>>>>>>>>>>>>>", mins)
        # Sleep for a minute
       # time.sleep(60)
        # Increment the minute total
       # mins += 1
    # Bring up the dialog box here

#!/usr/bin/env python
from random import randint
import time

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rnd = list(abc)
timer = input("Set timer (minutes): ")

def clock(timer):
	left = int(timer)
	while left!=0:
		# Sleep for a minute
		time.sleep(60)
		# Decrement the minute total
		left -= 1
		# Dialog box
		if (left != 1):
			print  str(left) + " minutes left"
		else:
			print "One minute!"
	print "\nTime!\n"

while rnd:
	raw_input("We are playing with letter...")
	print rnd.pop(randint(0,len(rnd)-1))
	clock(timer)
print "\nGame Over"
