#!/usr/bin/env python

import random
import array
import cowsay
from termcolor import cprint

cowsay.miki("NEED PASSWORD")
cprint("     [-]     Password Generator Tool     [-]", 'cyan')
cprint("     [-]    Created by Hakan Karabacak   [-]", 'cyan')
print("")
cprint("      Welcome to the Password Generator Tool.", 'magenta')
cprint("    The easiest way to get unbreakable passwords.", 'magenta')


MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                    'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
        '*', '(', ')', '<', '[', ']', '£', '^', '{', '}']

ans = True
while ans:
    print("""
    (?) Do You want to change password limit ? (default is 12) 
    """)
    ans = input("Please type y or n: ")
    if ans == "y":
        MAX_LEN = int(input("Your password limit: "))
        if MAX_LEN < 4:
            print("(!) Cannot be 4 or less (!)")
            break
    elif ans == "n":
        MAX_LEN == 12
    else:
        print("(!) Bad Input, generating with default settings... (!)")
    
    ans = False

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS  

random_digit = random.choice(DIGITS)
random_upper = random.choice(UPCASE_CHARACTERS)
random_lower = random.choice(LOCASE_CHARACTERS)
random_symbol = random.choice(SYMBOLS)

tmp_pass = random_digit + random_upper + random_lower + random_symbol


for x in range(MAX_LEN - 4):
    tmp_pass = tmp_pass + random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u', tmp_pass)
    random.shuffle(temp_pass_list)

password = ""

for x in temp_pass_list:
        password = password + x
        
print("(*) Your password has been created: ", password)

ans2 = True
while ans2:
    print("""
    r. Refresh
    q. Shutdown
    """)
    ans2 = input("(?) What would you like to do? (r or q): ")
    if ans2 == "r":
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS  

        random_digit = random.choice(DIGITS)
        random_upper = random.choice(UPCASE_CHARACTERS)
        random_lower = random.choice(LOCASE_CHARACTERS)
        random_symbol = random.choice(SYMBOLS)

        tmp_pass = random_digit + random_upper + random_lower + random_symbol


        for x in range(MAX_LEN - 4):
            tmp_pass = tmp_pass + random.choice(COMBINED_LIST)

            temp_pass_list = array.array('u', tmp_pass)
            random.shuffle(temp_pass_list)

        password = ""

        for x in temp_pass_list:
                password = password + x
        
        print("(*) Your password has been recreated: ", password)
    elif ans2 == "q":
        cprint("shutting down..", 'red')
        ans2 = False
        break
    else:
        print("(!) BAD INPUT (!)")
        