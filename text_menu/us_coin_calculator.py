# CODE FOR COIN CALCULATOR, PROVIDED THAT THE CURRENCY IS SET TO DOLLARS.
# --------------------------------------------------

# General_functions contains functions that are used throughout multiple parts of the program.

from general_functions import us_coins, us_coins_dict, get_cent_amount, floor_calc
# --------------------------------------------------

# Gets the coin-denomination that the user wants to turn their cents into.
# If the user enters anything other than a valid coin-denomination then get_denomination returns 
# 'incorrect_usage' so that the user can be re-prompted via a while-loop in main(config).

def get_denomination():
    denomination = input("What denomination? $2, $1, 50c, 20c or 10c? ")
    if denomination in us_coins:
        return denomination
    else:
        print("Please choose $2, $1, 50c, 20c or 10c.")
        return "incorrect_usage"
# --------------------------------------------------

# Given an amount of cents and a coin-denomination, coin_exchange prints 
# the number of said coins you can recieve in exchange for your cents,
# along with the amount of cents you will have left.

def coin_exchange(cents, denomination):
    coin_amount = floor_calc(cents, us_coins_dict[f"{denomination}"])
    cent_remainder = cents % us_coins_dict[f"{denomination}"]
    if cent_remainder == 0:
        if coin_amount == 1:
            print(f"You can exchange your cents for exactly {coin_amount} {denomination} coin.")       
        if coin_amount > 1:
            print(f"You can exchange your cents for exactly {coin_amount} {denomination} coins.")           
    elif coin_amount == 0:
        print("You don't have enough cents to exchange!")
    elif coin_amount == 1:
        print(f"You can exchange your cents for {coin_amount} {denomination} coin with {cent_remainder}c to spare.")
    else: 
        print(f"You can exchange your cents for {coin_amount} {denomination} coins with {cent_remainder}c to spare.")
    return 0
# --------------------------------------------------

# The main function:
# The user is prompted for the amount of cents they have to trade.
# They are then prompted for a coin-denomination. coin_exchange then calculates the amount of coins
# of that denomination the user can receive, along with the amount of cents they will have left over.
# This information is then printed in a human-readable format.

def main(config):
    cents = get_cent_amount(config)
    while cents < 0:
        cents = get_cent_amount(config)
    denomination = get_denomination()
    while denomination == "incorrect_usage":
        denomination = get_denomination()
    coin_exchange(cents, denomination)
# --------------------------------------------------


