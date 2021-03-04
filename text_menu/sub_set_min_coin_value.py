# CODE FOR SETTING THE MINIMUM COIN INPUT VALUE ( CHOICE 2 OF THE SUB-MENU )


# Gets the user to input a new minimum amount of coins that the user can enter 
# into the Coin Calulator and Mutiple Coin Calculator
def min_coin_value(config):
    try:
        min_coin = input("What is the minimum amount of coins you want the machine to accept? ")
        min_coin = int(min_coin)
        if int(min_coin) < 0:
            print("Request denied.")
            print("The minimum must be at least 0.")
            print()
            return -1
        if int(min_coin) >= 10000:
            print("Request denied.")
            print("You cannot set the minimum coin value to 10000 or larger.")
            print()
            return -2
        if int(min_coin) > config["max_coin_value"]:
            print("Request denied.")
            print("That is larger than the maximum coin amount!")
            print()
            return-3           
    except:
        print("Please enter a minimum amount of coins.")
        print()
        return -3
    return int(min_coin)


# Returns the number that the user has inputted, provided that the number is greater than 0. If
# the number is 0 or less then the user is re-prompted.
def main(config):
    min_coin = min_coin_value(config)
    while min_coin < 0:
        min_coin = min_coin_value(config)
    return min_coin

