# CODE FOR MULTIPLE COIN CALCULATOR, PROVIDED THAT THE CURRENCY IS SET TO POUNDS.
# --------------------------------------------------

# General_functions contains functions that are used throughout multiple parts of the program.

from general_functions import get_penny_amount ,floor_calc, uk_coins, uk_coins_dict
# --------------------------------------------------

# Gets the coin-denomination that the user wants to exclude.
# If an incorrect string is entered then exclude_denomination returns 'incorrect_usage'
# so that the user can be re-prompted via a while-loop in main(config). 

def exclude_denomination():
    denomination = input("What denomination do you wish to exclude? £2, £1, 50p, 20p or 10p? ")
    if denomination in uk_coins:
        return denomination
    else:
        print("Please choose £2, £1, 50p, 20p or 10p.")
        return "incorrect_usage"
# --------------------------------------------------

# Calculates the amount of each coin the user can receive for their pennies,
# prioritising the higher denominations.
# The results are returned in a list, uk_coins_amounts.
# Each entry in the list corresponds to the coin in the same entry of the list uk_coins.
# E.g uk_coins_amounts[1] corresponds to uk_coins[1], which is £1. 
# uk_coins_amounts is one element longer than uk_coins, however.
# The extra (final) element corresponds to theamount of pennies that are left over.
# The input excluded_denomination takes the denomination that needs to be exluded.
# E.g calculate(1234, £2) would exclude £2 and uk_coins_amounts would
# read [0, 12, 0, 1, 1, 4]. 12 £1 coins, 1 20p, 1 10p and 4 pence left over.

def calculate(pennies, excluded_denomination):
    uk_coins_amounts = []
    for i in range(0, len(uk_coins)):
        if uk_coins[i] != excluded_denomination:
            uk_coins_amounts.append(floor_calc(pennies, uk_coins_dict[uk_coins[i]]))
            pennies -= uk_coins_amounts[i] * uk_coins_dict[uk_coins[i]]
        else:
            uk_coins_amounts.append(0) 
    uk_coins_amounts.append(pennies)
    return uk_coins_amounts 
# --------------------------------------------------    

# result_print prints out the results of the list that the calculate function produces. 
# The results are printed in a human-readable format.

def result_print(uk_coins, uk_coins_amounts):
    print("Your pennies can be exchanged for ", end = "")
    for i in range(0, len(uk_coins)):
        if uk_coins_amounts[i] > 1:
            print(f"{uk_coins_amounts[i]} {uk_coins[i]} coins, ", end = "")
        elif uk_coins_amounts[i] == 1:
            print(f"{uk_coins_amounts[i]} {uk_coins[i]} coin, ", end = "")
    if uk_coins_amounts[-1] == 0:
        print("and you'll have no pennies left over!")
    else:
        if uk_coins_amounts[-1] != 1:
            print(f"and you'll have {uk_coins_amounts[-1]} pennies left over!")
        else:
            print(f"and you'll have {uk_coins_amounts[-1]} penny left over!")
# --------------------------------------------------

# The main function:
# First the user is prompted for the amount of pennies they have.
# They are then prompted for the denomination they wish to exclude.
# A list, uk_coins_amounts, is then created.
# This lists holds all the information about how many of each coin the user will receive.
# result_print then translates this information into a human-readable format. 

def main(config):
    pennies = get_penny_amount(config)
    while pennies < 0:
        pennies = get_penny_amount(config)
    excluded_denomination = exclude_denomination()
    while excluded_denomination == "incorrect_usage":
        excluded_denomination = exclude_denomination()
    uk_coins_amounts = calculate(pennies, excluded_denomination)
    result_print(uk_coins, uk_coins_amounts)
# --------------------------------------------------