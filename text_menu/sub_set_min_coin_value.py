

def min_coin_value():
    try:
        min_coin = input("What is the minimum amount of pennies you want the machine to accept? ")
        min_coin = int(min_coin)
        if int(min_coin) < 0:
            print("The minimum must be at least 0.")
            return -1
    except:
        print("Please enter a minimum amount of pennies.")
        return -3
    return int(min_coin)


def main():
    min_coin = min_coin_value()
    while min_coin < 0:
        min_coin = min_coin_value()
    return min_coin

