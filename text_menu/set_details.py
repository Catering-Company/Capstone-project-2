# general_functions contains functions that are used throughout multiple
# parts of the program. Headers for the min/max functions are also included.
from general_functions import option_chooser, spacer
import sub_set_min_coin_value
import sub_set_max_coin_value


# The length of the sub-menu
SUB_MENU_OPTIONS = 4


# Function to print out the sub-menu
def sub_menu():
    print("***Set Details Sub-Menu***")
    print("1 - Set currency")
    print("2 - Set minimum coin input value")
    print("3 - Set maximum coin input value")
    print("4 - Return to main menu")    
    print()


# Asks the user what their preffered currency is by requesting them to enter either 
# 'us dollars' or 'pounds sterling'. If the user enters anything else then 
# what_currency returns "incorrect-usage". A while-loop in main(config) will then 
# re-prompt the user until they enter either 'us dollars' or 'pounds sterling'.
def what_currency():
    currency = input("What is your preffered currency? Pounds Sterling or US Dollars? ")
    if currency.strip().lower() in {"pounds sterling", "us dollars"}:
        return currency.lower()
    else:
        return "incorrect-usage"


# The main function:
# The sub_menu is brought up and the user is prompted to choose an option via
# option_chooser, just as in main_menu.py. If the user enters anything other than
# 1 through to 4, then they will be re-prompted. 
#           - If the user enters 1 then what_currency will take effect. config will
#             update to the chosen currency. The user then returns to the sub-menu.
#             and the process is repeated.
#           - If the user enters 2 or 3 then the imported header files are used to
#             to prompt the user for a min or max coin value. config is then 
#             updated with the chosen min or max value. The user then returns to the
#             sub-menu and the process is repeated.
#           - If the user enters 4 then they are taken back to the main menu.
# Note: see general_functions for an explanation of config.   
def main(config):
    spacer()
    sub_menu()
    sub_choice = option_chooser(SUB_MENU_OPTIONS)
    while sub_choice not in range(1, SUB_MENU_OPTIONS + 1):
        sub_choice = option_chooser(SUB_MENU_OPTIONS)
    while sub_choice != SUB_MENU_OPTIONS:
        if sub_choice == 1:
            spacer()
            currency = what_currency()
            while currency == "incorrect-usage":
                print("Please enter either Pounds Sterling or US Dollars.")
                currency = what_currency()
            config["currency"] = currency.upper()     
        if sub_choice == 2:
            spacer()
            min_coin_value = 0
            min_coin_value = sub_set_min_coin_value.main()
            config["min_coin_value"] = min_coin_value
        if sub_choice ==3:
            spacer()
            max_coin_value = 10000
            max_coin_value = sub_set_max_coin_value.main()
            config["max_coin_value"] = max_coin_value
        print()
        input("Press enter to return to the sub-menu.")
        spacer()
        sub_menu()
        sub_choice = option_chooser(SUB_MENU_OPTIONS)
    return config
