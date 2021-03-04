# CODE FOR MULTIPLE COIN CALCULATOR, PROVIDED THAT THE CURRENCY IS SET TO DOLLARS


# general_functions contains functions that are used throughout multiple
# parts of the program.
from general_functions import get_cent_amount ,floor_calc, us_coins, us_coins_dict


# Gets the coin-denomination that the user wants to exclude. If an incorrect string is 
# entered then exclude_denomination returns 'incorrect_usage' so that the user can be
# re-prompted via a while-loop in main(config). 
def exclude_denomination():
    denomination = input("What denomination do you wish to exclude? $2, $1, 50c, 20c or 10c? ")
    if denomination in us_coins:
        return denomination
    else:
        print("Please choose $2, $1, 50c, 20c or 10c.")
        return "incorrect_usage"


# Calculates the amount of each coin the user can recieve for their cents, prioritising
# the higher denominations. The results are returned in a list, us_coins_amounts. Each 
# entry in the list corresponds to the coin in the same entry of the list us_coins. E.g
# us_coins_amounts[1] corresponds to us_coins[1], which is $1. us_coins_amounts is one 
# element longer than us_coins, however. The extra (final) element corresponds to the
# amount of cents that are left over.
# The input excluded_denomination takes the denomination that
# needs to be excluded. E.g calculate(1234, $2) would exclude $2 and us_coins_amounts would
# read [0, 12, 0, 1, 1, 4]. 12 $1 coins, 1 20c, 1 10c and 4 cents left over. 
def calculate(cents, excluded_denomination):
    us_coins_amounts = []
    for i in range(0, len(us_coins)):
        if us_coins[i] != excluded_denomination:
            us_coins_amounts.append(floor_calc(cents, us_coins_dict[us_coins[i]]))
            cents -= us_coins_amounts[i] * us_coins_dict[us_coins[i]]
        else:
            us_coins_amounts.append(0) 
    us_coins_amounts.append(cents)
    return us_coins_amounts 
    

# result_print prints out the results of the list that the calculate function produces. 
# The results are printed in a human-readable format.
def result_print(us_coins, us_coins_amounts):
    print("Your cents can be exchanged for ", end = "")
    for i in range(0, len(us_coins)):
        if us_coins_amounts[i] > 1:
            print(f"{us_coins_amounts[i]} {us_coins[i]} coins, ", end = "")
        elif us_coins_amounts[i] == 1:
            print(f"{us_coins_amounts[i]} {us_coins[i]} coin, ", end = "")
    if us_coins_amounts[-1] == 0:
        print("and you'll have no cents left over!")
    else:
        if us_coins_amounts[-1] != 1:
            print(f"and you'll have {us_coins_amounts[-1]} cents left over!")
        else:
            print(f"and you'll have {us_coins_amounts[-1]} cent left over!")


# The main function:
# First the user is prompted for the amount of cents they have. They are then prompted
# for the denomination they wish to exclude. A list, us_coins_amounts, is then created.
# This lists holds all the information about how many of each coin the user will receive.
# result_print then translates this information into a human-readable format. 
def main(config):
    cents = get_cent_amount(config)
    while cents < 0:
        cents = get_cent_amount(config)
    excluded_denomination = exclude_denomination()
    while excluded_denomination == "incorrect_usage":
        excluded_denomination = exclude_denomination()
    us_coins_amounts = calculate(cents, excluded_denomination)
    result_print(us_coins, us_coins_amounts)
