# GENERAL FUNCTIONS THAT ARE USED THROUGHOUT MULTIPLE PARTS OF THE PROGRAM

# --------------------------------------------------
# Global variables:
#
#
# A useful list and dictionary for both US and UK currency
uk_coins = ["£2", "£1", "50p", "20p", "10p"]
uk_coins_dict = {
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20,
        "10p": 10,
    }
us_coins = ["$2", "$1", "50c", "20c", "10c"]
us_coins_dict = {
        "$2": 200,
        "$1": 100,
        "50c": 50,
        "20c": 20,
        "10c": 10,
    }


# CONFIG is a constant list of the initial configurations of the program. In the main() section of
# main_menu.py, the list-variable config is set to equal CONFIG. config can be changed
# in the 'Set Details' section.  The values of config can be printed in the 'Display Program
# Configurations' section. config is used in the 'Coin Calculator' and the 'Multiple Coin
# Calculator' sections in order to ensure that the user enters an amount of pennies that falls 
# within the correct range. I.e if config["min_coin_value"] = 100 and 
# config["max_coin_value"] = 500 then the user will be reprompted if they don't enter an integer
# between 100 and 500.
# config also determines whether 'Coin Calculator' and 'Multiple Coin Calculator' run in pounds or
# dollars, based on what config["currency"] is set to.  
CONFIG = {
    "currency": "POUNDS STERLING",
    "min_coin_value": 0,
    "max_coin_value": 10000,
}
#---------------------------------------------------


#---------------------------------------------------
# Functions: 
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


# Creates a 'fresh' terminal window
def spacer():
        for i in range(0,100):
            print()


#Calculates the floor of x when divided by y
def floor_calc(x, y):
    return int((x / y) // 1)


# Gets the user to input the amount of pennies that they want to exchange. Ensures the user
# inputes a positive integer. get_penny_amount takes the parameter config. This parameter
# is a list that has a 'min_coin_value' and a 'max_coin_value' as keys. get_penny_amount
# will ensure that the amount of pennies the user chooses is between these values of 
# 'min_coin_value' and 'max_coin_value'.
def get_penny_amount(config):
    try:
        pennies = input("How many pennies do you have? Please enter a positive number: ")
        pennies = int(pennies)
        if int(pennies) < config["min_coin_value"]:
            print(f"The minimum coin value is set to {config['min_coin_value']}.")
            return -1
        if int(pennies) > config["max_coin_value"]:
            print(f"The maximum coin value is set to {config['max_coin_value']}.")
            return -2
        if int(pennies) <= 0:
            print("This is not a valid amount of pennies.")
            return -3
        if int(pennies) == 0:
            print("You need to have some pennies in order to exchange them!")
            return -4
    except:
        print("This is not a valid amount of pennies.")
        return -5
    return int(pennies)


# Same as get_penny_amount but with cents. 
def get_cent_amount(config):
    try:
        cents = input("How many cents do you have? Please enter a postiive number: ")
        cents = int(cents)
        if int(cents) < config["min_coin_value"]:
            print(f"The minimum coin value is set to {config['min_coin_value']}.")
            return -1
        if int(cents) > config["max_coin_value"]:
            print(f"The maximum coin value is set to {config['max_coin_value']}.")
            return -2
        if int(cents) <= 0:
            print("This is not a valid amount of cents.")
            return -3
        if int(cents) == 0:
            print("You need to have some cents in order to exchange them!")
            return -4
    except:
        print("This is not a valid amount of cents.")
        return -5
    return int(cents)

#---------------------------------------------------------