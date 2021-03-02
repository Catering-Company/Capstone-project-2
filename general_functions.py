# Global variables
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
    

# Allows the user to choose what option they want from the menu. The parameter is an integer
# that needs to equal the length of the menu. 
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
# inputes a positive integer.
def get_penny_amount():
    try:
        pennies = input("How many pennies do you have? Please enter a postiive number: ")
        pennies = int(pennies)
        if int(pennies) <= 0:
            print("This is not a valid amount of pennies.")
            return -1
        if int(pennies) == 0:
            print("You need to have some pennies in order to exchange them!")
            return -2
    except:
        print("This is not a valid amount of pennies.")
        return -3
    return int(pennies)