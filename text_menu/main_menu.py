# CODE FOR THE MAIN MENU
# --------------------------------------------------

# General_functions contains functions that are used throughout multiple parts of the program.
# The other headers contain the content for the respective options in the main menu.
from general_functions import spacer, option_chooser, CONFIG
import uk_coin_calculator
import uk_multiple_coin_calculator
import us_coin_calculator
import us_multiple_coin_calculator
import set_details
# --------------------------------------------------

# The amount of options in the main menu.
MENU_OPTIONS = 6

# Function to print the main menu.
def menu():
    print("***Coin Sorter - Main Menu***")
    print("1 - Coin calculator")
    print("2 - Multiple coin calculator")
    print("3 - Print coin list")
    print("4 - Set details")
    print("5 - Display program configurations")
    print("6 - Quit the program")
    print()
# --------------------------------------------------

# The main section:
# The main menu is printed. Using option_chooser, the user is prompted
# to choose a number between 1 and 6, correlating to the 6 choices they have been provided with.
# If the user chooses 1 through 5, they are taken to the chosen part of the program. 
# Once they are finished, they are taken back to the main menu and asked to choose a number between 1 and 6 once again.
# If they choose 1 through 5, repeat.
# If they choose 6, the program exits and thanks the user.
# Note that option_chooser will re-prompt the user.
# for a valid number if they don't enter an integer from 1 to 6. 
def main():
    #see general_functions.py for an explanation of config.
    config = CONFIG
    spacer()
    menu()
    choice = option_chooser(MENU_OPTIONS)
    while choice != MENU_OPTIONS:
        if choice == 1:
            spacer()
            # Note that config is used here to decide whether to use uk_coin_calculator or us_coin_calculator.
            # Config is also used to make analogous decisions when choice == 2, 3 and 5. 
            if config['currency'] == "POUNDS STERLING":
                uk_coin_calculator.main(config)
            if config['currency'] == "US DOLLARS":
                us_coin_calculator.main(config)
        if choice == 2:
            spacer()
            if config['currency'] == "POUNDS STERLING":
                uk_multiple_coin_calculator.main(config)
            if config['currency'] == "US DOLLARS":
                us_multiple_coin_calculator.main(config)
        if choice == 3:
            spacer()
            print("The following coins are currently in circulation:")
            if config['currency'] == "POUNDS STERLING":
                print("£2, £1, 50p, 20p, 10p.")
            if config['currency'] == "US DOLLARS":
                print("$2, $1, 50c, 20c, 10c")
        if choice == 4:
            config = set_details.main(config)
        if choice == 5:
            spacer()
            print(f"Currency: {config['currency']}")
            if config['currency'] == "POUNDS STERLING":
                print(f"Minimum amount of pennies: {config['min_coin_value']}")
                print(f"Maximum amount of pennies: {config['max_coin_value']}")
            if config['currency'] == "US DOLLARS":
                print(f"Minimum amount of cents: {config['min_coin_value']}")
                print(f"Maximum amount of cents: {config['max_coin_value']}")
        print()
        input("Press enter to return to the main menu.")
        spacer()
        menu()
        choice = option_chooser(MENU_OPTIONS)
    spacer()
    print("Thank you for using!")
    print()        
# --------------------------------------------------
        
main()
