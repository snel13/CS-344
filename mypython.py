#!/usr/bin/env python

#Assignment: 5- Python exploration 
#Author: Sam Nelson
#Description: Create 3 files, fill each of the files with 10 random characters non space lowercase characters
#Print contents of 3 files on screen that are filling each of the files, then print two random ints to screen from subset
#[1-42] then print product of two numbers.

#We will need the random and string modules
import random
import string
print("\n10 Random letters per row in console, correlates to each file:")
#Loop below will loop 3 times and then exit (1,4) is really [1,4) which means include 1 exclude 4 (so go to 3).  
#loop will do 4 things each itteration, it will create a file with the loop itteration as part of the name
#loop will create a random string of 10 lowercase alphabetic lowercase letters
#loop will write this string to the file (file closes automatically)
#loop will finally print that same string to console
for num in range(1,4):
	f = open("file_"+str(num)+".txt","w")
	letters = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
	f.write(''.join(letters))
	print(letters)
#generate two random ints; by default the start is included and the stop is excluded so we want to go 1-42 really.
print("\n\tRandom Numbers [1-41]: \t")
intOne=random.randrange(1,42)
intTwo=random.randrange(1,42)
print(intOne)
print(intTwo)
print("\nThe Product of {0} * {1} = {2}\n".format(intOne, intTwo, intOne * intTwo))

