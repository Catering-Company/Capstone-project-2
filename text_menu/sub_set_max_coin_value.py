# CODE FOR SETTING THE MAXIMUM COIN INPUT VALUE ( CHOICE 3 OF THE SUB-MENU )

# Gets the user to input a new maximum amount of coins that the user can enter 
# into the Coin Calulator and Mutiple Coin Calculator
def max_coin_value():
    try:
        max_coin = input("What is the maximum amount of coins you want the machine to accept? ")
        max_coin = int(max_coin)
        if int(max_coin) < 0:
            print("The maximum must be at least 1.")
            return -1
    except:
        print("Please enter a maximum amount of coins.")
        return -3
    return int(max_coin)

# Returns the number that the user has inputted, provided that the number is greater than 0. If
# the number is 0 or less then the user is re-prompted.
def main():
    max_coin = max_coin_value()
    while max_coin < 0:
        max_coin = max_coin_value()
    return max_coin
