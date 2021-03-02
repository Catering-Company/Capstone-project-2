

def max_coin_value():
    try:
        max_coin = input("What is the maximum amount of pennies you want the machine to accept? ")
        max_coin = int(max_coin)
        if int(max_coin) < 0:
            print("The maximum must be at least 1.")
            return -1
    except:
        print("Please enter a maximum amount of pennies.")
        return -3
    return int(max_coin)


def main():
    max_coin = max_coin_value()
    while max_coin < 0:
        max_coin = max_coin_value()
    return max_coin
