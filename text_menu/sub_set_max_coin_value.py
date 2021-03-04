# CODE FOR SETTING THE MAXIMUM COIN INPUT VALUE ( CHOICE 3 OF THE SUB-MENU )

# Gets the user to input a new maximum amount of coins that the user can enter 
# into the Coin Calulator and Mutiple Coin Calculator. There are restrictions
# in place to prevent the user from entering:
# - Any non-integer.
# - A max value less than 0.
# - A max value greater than 10000.
# - A max value less than the current min value. 
#  If any of the above happens then min_coin_value returns a negative integer. A
#  while-loop in main(config) will then rerun min_coin_value.
def max_coin_value(config):
    try:
        max_coin = input("What is the maximum amount of coins you want the machine to accept? ")
        max_coin = int(max_coin)
        if int(max_coin) < 0:
            print("Request Denied.")
            print("The maximum must be a positive number!")
            print()
            return -1
        if int(max_coin) > 10000:
            print("Request Denied.")
            print("The maximum cannot exceed 10000.")
            print()
            return -2
        if max_coin < config["min_coin_value"]:  
            print("Request denied.")
            print("That is smaller than the minimum coin amount!")
            print()
            return -3
    except:
        print("Please enter a maximum amount of coins.")
        print()
        return -3
    return int(max_coin)


# Returns the number that the user has inputted, provided that the number is greater than 0. If
# the number is 0 or less then the user is re-prompted.
def main(config):
    max_coin = max_coin_value(config)
    while max_coin < 0:
        max_coin = max_coin_value(config)
    return max_coin
