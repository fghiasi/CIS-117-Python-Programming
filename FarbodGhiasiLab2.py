###########################################################
#
# Name: Farbod Ghiasi
# Course: CIS 117 Python Programming Lab #2
# Lab 2: Loops and Functions
# Term: Summer
# Lab Solution file: FarbodGhiasiLab2.py
# Development Env: Ubuntu 18.04
# Version: Python 3.6.5
# Date: Jun/24/2018
# Description: This program using functions, and loops
#              is trying to ask a user to enter a password
#               then validate it using these conditions:
#               1- is it 8 char long. 2- has at least one uppercase
#               and lowercase letter 3- has at least one digit. 4-
#               does the 2 entered pass match. If not as user to try
#               again.
#
###########################################################


# Return true if pass satisfies min char length requirement
def has_min_length(password):

    MIN_LENGTH = 8

    if len(password) < MIN_LENGTH:

        display_error("=> The password must be at least 8 characters long.")

    return len(password) >= MIN_LENGTH


# Return True if pass has at least one upper case
def is_upper_case(password):

    for letter in password:

        if letter.isupper():

            return True

    display_error("=> The password must have at least one uppercase.")

    return False


# Return True if pass has at least one lower case
def is_lower_case(password):

    for letter in password:

        if letter.islower():

            return True

    display_error("=> The password must have at least one lowercase.")
    return False


# Return True if pass has at least one digit
def has_digit(password):

    for letter in password:

        if letter.isdigit():

            return True

    display_error("=> The password must have at least one digit.")

    return False


# ask user to re-enter pass and return True if it matched
def is_match(password):

    re_enter_password = get_password("\n=> Please re-enter the password to "
                                     "match.")

    if password != re_enter_password:

        display_error("The two password didn't match.")

    return password == re_enter_password


# Return True if pass meet all requirements
def have_requirements(password):

    return is_lower_case(password) and \
           is_upper_case(password) and \
           has_digit(password) and \
           has_min_length(password) and \
           is_match(password)


# Get pass. show specific message.
def get_password(display_message):
    return input(display_message + "\n")


def display_error(error_text):

    print("\n" + error_text + "\n")


# Print requirements.
print("=> The password must be at least 8 characters long.\n"
      "=> The password must have at least one uppercase and one "
      "lowercase letter.\n=> The password must have at least one digit.\n")


# get pass for the first time.
password = get_password("Please Enter a password considering above "
                        "conditions:")

# ask user to correct the pass to meet requirement
while not have_requirements(password):
    password = get_password("Try again: Please Enter a password.")

# Print the pass will work.
print("That pair of passwords will work.")


'''
=> The password must be at least 8 characters long.
=> The password must have at least one uppercase and one lowercase letter.
=> The password must have at least one digit.

Please Enter a password considering above conditions:
farbod

=> The password must have at least one uppercase.

Try again: Please Enter a password.
Farbod

=> The password must have at least one digit.

Try again: Please Enter a password.
Farbod1

=> The password must be at least 8 characters long.

Try again: Please Enter a password.
Farbod12

=> Please re-enter the password to match.
Farbod21

The two password didn't match.

Try again: Please Enter a password.
Farbod12

=> Please re-enter the password to match.
Farbod12
That pair of passwords will work.

'''