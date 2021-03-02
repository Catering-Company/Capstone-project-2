# general_functions contains functions that are used throughout multiple
# parts of the program.
from general_functions import uk_coins, uk_coins_dict, get_penny_amount, floor_calc


# Gets the coin-denomination that the user wants to turn their pennies into
def get_denomination():
    denomination = input("What denomination? £2, £1, 50p, 20p or 10p? ")
    if denomination in uk_coins:
        return denomination
    else:
        print("Please choose £2, £1, 50p, 20p or 10p.")
        return "incorrect_usage"


# Given an amount of pennies and a coin-denomination, coin_exchange prints 
# the number of said coins you can recieve in exchange for your pennies, along
# with the amount of pennies you will have left. 
def coin_exchange(pennies, denomination):
    coin_amount = floor_calc(pennies, uk_coins_dict[f"{denomination}"])
    penny_remainder = pennies % uk_coins_dict[f"{denomination}"]
    if penny_remainder == 0:
        if coin_amount == 1:
            print(f"You can exchange your pennies for exactly {coin_amount} {denomination} coin.")       
        if coin_amount > 1:
            print(f"You can exchange your pennies for exactly {coin_amount} {denomination} coins.")           
    elif coin_amount == 0:
        print("You don't have enough pennies to exchange!")
    elif coin_amount == 1:
        print(f"You can exchange your pennies for {coin_amount} {denomination} coin with {penny_remainder}p to spare.")
    else: 
        print(f"You can exchange your pennies for {coin_amount} {denomination} coins with {penny_remainder}p to spare.")
    return 0


# The main function:
# The user is prompted for the amount of pennies they have to trade. They are then
# prompted for a coin-denomination. coin_exchange then calculates the amount of coins
# of that denomination the user can recieve, along with the amount of pennies
# they will have left over. This information is then printed in a human-readable format.
def main():
    pennies = get_penny_amount()
    while pennies < 0:
        pennies = get_penny_amount()
    denomination = get_denomination()
    while denomination == "incorrect_usage":
        denomination = get_denomination()
    coin_exchange(pennies, denomination)



