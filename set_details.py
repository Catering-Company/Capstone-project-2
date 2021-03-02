from general_functions import option_chooser, spacer


SUB_MENU_OPTIONS = 4

def sub_menu():

    print("***Set Details Sub-Menu***")
    print("1 - Set currency")
    print("2 - Set minimum coin input value")
    print("3 - Set maximum coin input value")
    print("4 - Return to main menu")    
    print()

def what_currency():
    currency = input("What is your preffered currency? Pounds sterling or US dollars? ")
    if currency.strip().lower() in {"pounds sterling", "us dollars", "dollars", "pounds"}:
        return currency.lower()
    else:
        return "incorrect-usage"

def main():
    sub_menu()
    choice = option_chooser(SUB_MENU_OPTIONS)
    while choice not in range(1, SUB_MENU_OPTIONS + 1):
        choice = option_chooser(SUB_MENU_OPTIONS)
    while choice != SUB_MENU_OPTIONS:
        if choice == 1:
            currency = what_currency()
            while currency == "incorrect-usage":
                currency == what_currency           
        print()
        input("Press enter to return to the sub-menu.")
        sub_menu()
        choice = option_chooser(SUB_MENU_OPTIONS)
    return currency
