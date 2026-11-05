# write a program that askes the user for thier name, and then adds it to a guest_list.txt file

user_name = input("What is your name? ")

with open('guest_list.txt', 'a') as list:
    list.write(user_name + '\n')




