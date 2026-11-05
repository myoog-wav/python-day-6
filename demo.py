# Escape Characaters \n

# print("Dear class, \n I am so sad say to say this is our last day.")

#Absolute v.s. relative. Pwd prints a path like /Users/huckborden/etc. it is absolute cause it is from home, above the users.
# relative is like cd .. its a path that depends on where we are. data/data.txt. always use relative file.

# Modules and Libraries. 
# Cool built in stuff with python. but want to use a tool that python didn;t include or a tool that python did include.

# python doesn't have that, we need to import it. read the documentation.

'''import random

random_int = random.randint(1, 10)
print(random_int)

deck_of_cards = ['King of Spades', '8 of hearts', '2 of diamonds']

random_card = random.choice(deck_of_cards)
print(random_card)

import math

answer_1 = math.sqrt(64)
print(answer_1)'''

# File Input/Output. I/O.

# We can store the values outside of the code. data that stays after the progam stops or ends. we need to write to a file or database. 
# reading, writing, append. reading we get the thing. Writing will overwite everything, if we want to keep we want to append. adding onto the end.

# with write() we have to specify if we want to a or w.

#with open("demo.txt", "a") as file:
#    file.write('File I/O is awesome.\n')

# chall

# finding password

line_count = 0
with open("demo.txt", "r") as file:
    for each_line in file:
        line_count = line_count + 1
        if "password" in each_line:
            print(each_line)
            print('the line number is,', line_count)

# challenge 2, create a file called line_counter.py. copy and paste song lyrics into a lyrics.txt file. output the TOTAL number of lines

