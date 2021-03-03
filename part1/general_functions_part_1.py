# GENERAL FUNCTIONS THAT ARE USED THROUGHOUT MULTIPLE PARTS OF THE PROGRAM

# --------------------------------------------------
# Global variables:
#
#
# A useful list and dictionary for UK currency
uk_coins = ["£2", "£1", "50p", "20p", "10p"]
uk_coins_dict = {
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20,
        "10p": 10,
    }
#---------------------------------------------------------


#---------------------------------------------------------
# Functions for the coin_calculator and multiple_coin_calculator:
#
#
# Gets the user to input the amount of pennies that they want to exchange. Ensures the user
# inputes a positive integer. This parameter
# is a list that has a 'min_coin_value' and a 'max_coin_value' as keys. get_penny_amount
# will ensure that the amount of pennies the user chooses is between these values of 
# 'min_coin_value' and 'max_coin_value'.
def get_penny_amount():
    try:
        pennies = input("How many pennies do you have? Please enter a positive number: ")
        pennies = int(pennies)
        if int(pennies) <= 0:
            print("This is not a valid amount of pennies.")
            return -3
        if int(pennies) == 0:
            print("You need to have some pennies in order to exchange them!")
            return -4
        if int(pennies) > 10000:
            print("The maximum coin value is set to 10000.")
            return -5
    except:
        print("This is not a valid amount of pennies.")
        return -5
    return int(pennies)
#
#
#Calculates the floor of x when divided by y
def floor_calc(x, y):
    return int((x / y) // 1)
#-------------------------------------------------------------


#-------------------------------------------------------------
#Functions that may help you create the list:
#
#
# Allows the user to choose what option they want from a menu. The parameter 'choices' is an
# integer that needs to equal the length of the menu. In 'main_menu.py' choices takes the value 
# of 6, whereas in 'set_details.py' choices takes the value of 4. If the user enters anything
# that isn't an integer from 1 through to choices then option_chooser returns a negative value
# so that the user can be re-prompted via a while-loop.
def option_chooser(choices):
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        if choice in range(1,choices + 1):
            return choice
    except:
        print()
        print("Invalid choice. Please try again.")
        return -1
    print()    
    print("Invalid choice. Please try again.")
    return -2
#
#
# Creates a 'fresh' terminal window
def spacer():
        for i in range(0,100):
            print()
#---------------------------------------------------------