# general_functions contains functions that are used throughout multiple
# parts of the program.
from general_functions import option_chooser, spacer
import sub_set_min_coin_value
import sub_set_max_coin_value

SUB_MENU_OPTIONS = 4

def sub_menu():
    print("***Set Details Sub-Menu***")
    print("1 - Set currency")
    print("2 - Set minimum coin input value")
    print("3 - Set maximum coin input value")
    print("4 - Return to main menu")    
    print()


def what_currency():
    currency = input("What is your preffered currency? Pounds Sterling or US dollars? ")
    if currency.strip().lower() in {"pounds sterling", "us dollars"}:
        return currency.lower()
    else:
        return "incorrect-usage"

def main(config):
    spacer()
    sub_menu()
    choice = option_chooser(SUB_MENU_OPTIONS)
    while choice not in range(1, SUB_MENU_OPTIONS + 1):
        choice = option_chooser(SUB_MENU_OPTIONS)
    while choice != SUB_MENU_OPTIONS:
        if choice == 1:
            currency = what_currency()
            while currency == "incorrect-usage":
                currency == what_currency
            config["currency"] = currency.upper()     
        if choice == 2:
            spacer()
            min_coin_value = 0
            min_coin_value = sub_set_min_coin_value.main()
            config["min_coin_value"] = min_coin_value
        if choice ==3:
            spacer()
            max_coin_value = 10000
            max_coin_value = sub_set_max_coin_value.main()
            config["max_coin_value"] = max_coin_value

        print()
        input("Press enter to return to the sub-menu.")
        spacer()
        sub_menu()
        choice = option_chooser(SUB_MENU_OPTIONS)
    return config
