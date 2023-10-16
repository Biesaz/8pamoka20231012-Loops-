# # For loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# # loop through lists
# names = ["Albert", "Tom", "Leonardo"]
# for vardas in names:
#     print(f"Greetings, {vardas}")

# # loop through strings
# name = "Code Academy"
# for raidems in name :
#     print(raidems)

# # loop through dictionaries:
# my_dict = {"name": "Albert", "role": "scientist", "surname": "Jonaitis", "sport": "futbolist"}
# for key, value in my_dict.items():
#     print(key, value)

# # loop through sets, tuples:
# it is exactly the same as with the lists

# names = ("Albert", "Tom", "Leonardo")
# for name in names:
#     print(f"Greetings, {name}")
# names = {"Albert", "Tom", "Leonardo"}
# for name in names:
#     print(f"Greetings, {name}")

# #range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# Syntax
# range(start, stop, step)

# argument	meaning
# start 	Optional. An integer number specifying at which position to start. Default is 0
# stop	    Required. An integer number specifying at which position to stop (not included).
# step	    Optional. An integer number specifying the incrementation. Default is 1

# x = range(3, 6)
# for n in x:
#   print(n)

# for n in range(0, 10, 2):
#   print(n)

# # break
# With the break statement we can stop the loop even if the while condition is true:
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 0.

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# # continue
# With the continue statement we can stop the current iteration, and continue with the next:

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# 🧠 Excercises

# 1.
# Create a variables containing strings for username and password. 
# Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.

# all_users = {"aaa": "111", "bbb": "222", "ccc": "333"}
# while True:
#     entered_username = input("Enter your username: ")
#     entered_password = input("Enter your password: ")
#     # if username in all_users and all_users[username] == password: # si eilute is GPTchat
#     for username, password in all_users.items():
#         if entered_username == username and entered_password == password:
#             print("welcome")
#             break
#         else:
#             print("Wrong")   
 
# 2.
# Allow user to enter 10 integers, and then print the sum and average of those entered numbers.

# list_of_ten_integers = []
# print("Enter 10 numbers: ")
# for numbers in range(10):
#     entered_numbers = int(input())
#     list_of_ten_integers.append(entered_numbers)
# sum_of_ten_integers = sum(list_of_ten_integers)
# average_of_ten_integers = sum_of_ten_integers / len(list_of_ten_integers)
# print("The sum of the entered 10 numbers is:", sum_of_ten_integers)
# print("The average of the entered 10 numbers is:", average_of_ten_integers)

# 3.
# Generate a dictionary of 10 keys being 1,2,3...10 each of them should store a value of random integer number from 1 to 100.

# dictionary_of_ten_keys = {}
# list_of_ten_keys = [] 
# key = 1
# while key < 11:
#     list_of_ten_keys.append(key)
#     key += 1
# import random
# list_of_ten_random_values = []   
# for value in range(10):
#     random_number = random.randint(1, 100)
#     list_of_ten_random_values.append(random_number)
#     dictionary_of_ten_keys = dict(zip(list_of_ten_keys, list_of_ten_random_values))
# print(dictionary_of_ten_keys)

# 4.
# Create a pin code cracker. Let's say pin code consists of 4 random digits. You can store the value in variable. 
# Then create a loop going through all possible combinations until you find the one you entered.

# import random
# list_of_pin = []   
# for value in range(4):
#     random_number = random.randint(1, 4)
#     list_of_pin.append(random_number)
#     print(list_of_pin)

# import itertools           # GPTchat
# # Define the pin code length.
# PIN_CODE_LENGTH = 4
# # Get the pin code from the user.
# pin_code = input("Enter the pin code: ")
# # Generate all possible combinations of the pin code.possible_pin_codes = []
# for i in range(PIN_CODE_LENGTH):
#   for digit in range(10):
#     possible_pin_codes.append(str(digit))
# # Iterate over all possible pin codes and check if it matches the entered pin code.
# for possible_pin_code in possible_pin_codes:
#   if possible_pin_code == pin_code:
#     print("The pin code is:", possible_pin_code)
#     break
# # If no matching pin code is found, print a message to the user.
# else:
#   print("The pin code is not valid.")


# pin = 1111  #Sauliaus
# i = 0
# while i != pin:
#     i =+ 1
# print()

# import time   #Renato
# start_time = time.time()
# while True:
#     pin_code = int(input("enter"))
#     for numbers in range(0, 1000):
#         print(numbers)
#         if number == pin_code:
#             break
#     end_time = time.time()
#     print("lux")  

# Mykolo
# all_users = {"aaa": "111", "bbb": "222", "ccc": "333"}
# value = True
# while value == True:
#     entered_username = input("Enter your username: ")
#     entered_password = input("Enter your password: ") 
#     for username, password in all_users.items():
#         if entered_username == username and entered_password == password:
#             print("Welcome")
#             break
# value = False
# print("Wrong")
# Vytauto
# all_users = {"aaa": "111", "bbb": "222", "ccc": "333"}
# while True:
#     entered_username = input("Enter your username: ")
#     entered_password = input("Enter your password: ")
#     for username, password in all_users.items():
#         user_exists = entered_username == username and entered_password == password
#         if user_exists:
#             print:("welcome")

# Mykolo 
# Task number 3
# random_dict = {}
# for i in range(1,11):
#     random_dict[i] = random.randint(1,100)
#     print(random_dict)
    
#Task number 4
# import time
# pin = '1010'
# locked = Truestart_time = time.perf_counter()
# while locked:
#         for digit1 in range(10):
#             for digit2 in range(10):
#                 for digit3 in range(10):
#                     for digit4 in range(10):
#                         current_attempt = f"{digit1}{digit2}{digit3}{digit4}"  
#                         if current_attempt == pin:
#                             print(f"Pin Cracked! The correct pin is: {current_attempt}") 
#         break
# locked = Falseend_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f'Elapsed time: {elapsed_time} seconds')

# Renato
# import time
# while True:
#     pin_code = int(input("Enter your number from 0 to 1000000: "))
#     start_time = time.time()
#     for number in range(-1, 1000001):
#         print(number)
#         if  number == pin_code:
#             break
#         end_time = time.time()
#         print("I guess your number was: ", number, "Time to bruteforce: ", end_time-start_time)
#     play_again = input("Do you want to try again ? (yes/no): ")
#     if play_again.lower() == "yes":
#         print("Super, lets have a fun ! ")
#     elif play_again.lower() == "no":
#         print ("It's a pitty, see you next time !")
#         break

# import random
# numbers_dictionary = {}
# for number in range(1,10):
#     random_value = random.randint(1, 100)
#     numbers_dictionary[number] = random_value
#     print(numbers_dictionary)

# Sauliaus
# pin = "9235"
# chars = ["1","2","3","4","5","6","7","8","9","0"]
# pin_guse = []
# for simb in pin:
#     for si in chars:
#         if si == simb:
#             pin_guse.append(si)
# print(pin_guse)


