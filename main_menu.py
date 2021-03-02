# general_functions contains functions that are used throughout multiple
# parts of the program. The other headers contain the content for the respective
# options in the main menu
from general_functions import spacer, option_chooser
import coin_calculator
import multiple_coin_calculator
import set_details


# The amount of options in the main menu
MENU_OPTIONS = 6


# Function to print the main menu 
def menu():
    spacer()
    print("***Coin Sorter - Main Menu***")
    print("1 - Coin calculator")
    print("2 - Multiple coin calculator")
    print("3 - Print coin list")
    print("4 - Set details")
    print("5 - Display program configurations")
    print("6 - Quit the program")
    print()


# The main section:
# The main menu is printed. Using option_chooser, the user is prompted
# to choose a number between 1 and 6, correllating to the 6 choices they have been provided
# with. If the user chooses 1 through 5, they are taken to the chosen part of the 
# program. Once they are finished, they are taken back to the main menu and asked to choose
# a number between 1 and 6 once again.  If they choose 1 through 5, repeat. If they choose
# 6, the program exits and thanks the user. Note that option_chooser will re-prompt the user
# for a valid number if they don't enter an integer from 1 to 6. 
def main():
    menu()
    choice = option_chooser(MENU_OPTIONS)
    while choice != MENU_OPTIONS:
        if choice == 1:
            spacer()
            coin_calculator.main()
        if choice == 2:
            spacer()
            multiple_coin_calculator.main()
        if choice == 3:
            spacer()
            print("The following coins are currently in circulation:")
            print("£2, £1, 50p, 20p, 10p.")
        if choice == 4:
            spacer()
            set_details.main()
        if choice == 5:
            spacer()
            print("The currency is currently set to pounds sterling.")   
        print()
        input("Press enter to return to the main menu.")
        menu()
        choice = option_chooser(MENU_OPTIONS)
    spacer()
    print("Thank you for using!")
    print()        
        
        
main()
