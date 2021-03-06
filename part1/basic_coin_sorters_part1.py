# basic coin sorter for part 1
#---------------------------------------------------------

# Module need for to request currency data. Module for working with json also.
import requests

# Hidden Api key. Key is hidden for security
Api_key_file = open('./Apikey.txt', 'r')
Api_key = Api_key_file.read()

# This is a callable function that gets live currency rates for GBP to USD and also GBP to MGA. 
# It is important it is a function so the rates are live every time they are called.
# The output will be a dictionary which can be referenced and will allow more rates to be added if neccessary.
def Get_Currency_Rates():
    # Get request for currency data. Request will return a JSON
    data = requests.get('http://api.currencylayer.com/live?access_key='+Api_key+'&currencies=GBP,MGA&format=1')
    parsed_data = data.json()
    # Output will be how many USD to 1 GBP
    GBP_USD = 1/parsed_data['quotes']['USDGBP']
    # Output will be how many MGA to 1 GBP
    GBP_MGA = parsed_data['quotes']['USDMGA'] * GBP_USD
    # Dictionary that can be imported and used for conversion rates accross the project
    conversion_rates = {
        'GBP_USD':GBP_USD, 
        'GBP_MGA':GBP_MGA
        }
    # Will return dictionary of currency pair rates requested
    return conversion_rates

#---------------------------------------------------------

# CONFIG is a constant list of the initial configurations of the program. In this program it cannot be changed
 
CONFIG = {
    "currency": "POUNDS STERLING",
    "min_coin_value": 0,
    "max_coin_value": 10000,
}
# Global variables:
# A useful list and dictionary for UK currency
uk_coins = ["£2", "£1", "50p", "20p", "10p"]
uk_coins_dict = {
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20,
        "10p": 10,
    }

#---------------------------------------------------------

# Functions for the coin_calculator and multiple_coin_calculator:
# Gets the user to input the amount of pennies that they want to exchange. 
# Ensures the user inputs a positive integer. 
# This parameter is a list that has a 'min_coin_value' and a 'max_coin_value' as keys. 
# get_penny_amount will ensure that the amount of pennies the user chooses is between these values of 
# 'min_coin_value' and 'max_coin_value'.
def get_penny_amount():
    try:
        pennies = input("How many pennies do you have? Please enter a positive number: ")
        pennies = int(pennies)
        if int(pennies) < 0:
            print("This is not a valid amount of pennies.")
            return -3
        if int(pennies) == 0:
            print("You need to have some pennies in order to exchange them!")
            return -4
        if int(pennies) > 10000:
            print("The maximum coin value is set to 10000.")
            return -5
    except:
        print("This is not a valid amount of pennies.")
        return -5
    return int(pennies)


def get_pounds_amount():
    pounds_amount = 0
    try:
        pounds = input("Please enter the amount you wish to convert, in Pounds Sterling, between 0.00 and 100.00: ")
        pounds = round(float(pounds), 2)
        if pounds > 0 and pounds <= 100:
            pounds_amount = pounds
            return pounds_amount
        if pounds < 0:
            print("This is not a valid amount of Pounds.")
        if pounds == 0:
            print("You need to have some Pounds in order to convert them!")
        if pounds > 100:
            print("The maximum Pounds value is set to 100.")
    except:
        print("This is not a valid amount of Pounds.")
    return pounds_amount

# Gets the coin-denomination that the user wants to turn their pennies into. 
# If the user enters anything other than a valid coin-denomination then get_denomination returns 
# 'incorrect_usage' so that the user can be re-prompted via a while-loop in main().
def get_denomination():
    denomination = input("What denomination? £2, £1, 50p, 20p or 10p? ")
    if denomination in uk_coins:
        return denomination
    else:
        print("Please choose £2, £1, 50p, 20p or 10p.")
        return "incorrect_usage"

#Calculates the floor of x when divided by y
def floor_calc(x, y):
    return int((x / y) // 1)

# Given an amount of pennies and a coin-denomination, coin_exchange prints 
# the number of said coins you can receive in exchange for your pennies, along
# with the amount of pennies you will have left. 
def coin_exchange(pennies, denomination):
    coin_amount = floor_calc(pennies, uk_coins_dict[f"{denomination}"])
    penny_remainder = pennies % uk_coins_dict[f"{denomination}"]
    
    # Variables containing currency conversions
    GBPUSD = Get_Currency_Rates()['GBP_USD']
    GBPMGA = Get_Currency_Rates()['GBP_MGA']
    pennies_converted_to_USD = round((pennies/100) * GBPUSD, 2)
    pennies_converted_to_MGA = round((pennies/100) * GBPMGA, 2)
    if penny_remainder == 0:
        if coin_amount == 1:
            print(f"You can exchange your pennies for exactly {coin_amount} {denomination} coin.")
            print(f"In US Dollars that is {pennies_converted_to_USD}")
            print(f"In Malagasy Ariary that is {pennies_converted_to_MGA}")
        if coin_amount > 1:
            print(f"You can exchange your pennies for exactly {coin_amount} {denomination} coins.")
            print(f"In US Dollars that is {pennies_converted_to_USD}")
            print(f"In Malagasy Ariary that is {pennies_converted_to_MGA}")           
    elif coin_amount == 0:
        print("You don't have enough pennies to exchange!")
    elif coin_amount == 1:
        print(f"You can exchange your pennies for {coin_amount} {denomination} coin with {penny_remainder}p to spare.")
        print(f"In US Dollars that is {pennies_converted_to_USD}")
        print(f"In Malagasy Ariary that is {pennies_converted_to_MGA}")
    else: 
        print(f"You can exchange your pennies for {coin_amount} {denomination} coins with {penny_remainder}p to spare.")
        print(f"In US Dollars that is {pennies_converted_to_USD}")
        print(f"In Malagasy Ariary that is {pennies_converted_to_MGA}")
    return 0


# Gets the coin-denomination that the user wants to exclude. If an incorrect string is 
# entered then exclude_denomination returns 'incorrect_usage' so that the user can be
# re-prompted via a while-loop in main(). 
def exclude_denomination():
    denomination = input("What denomination do you wish to exclude? £2, £1, 50p, 20p or 10p? ")
    if denomination in uk_coins:
        return denomination
    else:
        print("Please choose £2, £1, 50p, 20p or 10p.")
        return "incorrect_usage"

# Calculates the amount of each coin the user can receive for their pennies, prioritising
# the higher denominations. The results are returned in a list, uk_coins_amounts. Each 
# entry in the list corresponds to the coin in the same entry of the list uk_coins. E.g
# uk_coins_amounts[1] corresponds to uk_coins[1], which is £1. uk_coins_amounts is one 
# element longer than uk_coins, however. The extra (final) element corresponds to the
# amount of pennies that are left over.
# The input excluded_denomination takes the denomination that
# needs to be exluded. E.g calculate(1234, £2) would exclude £2 and uk_coins_amounts would
# read [0, 12, 0, 1, 1, 4]. 12 £1 coins, 1 20p, 1 10p and 4 pence left over. 
def calculate(pennies, excluded_denomination):
    uk_coins_amounts = []
    for i in range(0, len(uk_coins)):
        if uk_coins[i] != excluded_denomination:
            uk_coins_amounts.append(floor_calc(pennies, uk_coins_dict[uk_coins[i]]))
            pennies -= uk_coins_amounts[i] * uk_coins_dict[uk_coins[i]]
        else:
            uk_coins_amounts.append(0) 
    uk_coins_amounts.append(pennies)
    return uk_coins_amounts 

# result_print prints out the results of the list that the calculate function produces. 
# The results are printed in a human-readable format.
def result_print(uk_coins, uk_coins_amounts, pennies):
    # Variables containing currency conversions
    GBPUSD = Get_Currency_Rates()['GBP_USD']
    GBPMGA = Get_Currency_Rates()['GBP_MGA']
    pennies_converted_to_USD = round((pennies/100) * GBPUSD, 2)
    pennies_converted_to_MGA = round((pennies/100) * GBPMGA, 2)
    print("Your pennies can be exchanged for ", end = "")
    for i in range(0, len(uk_coins)):
        if uk_coins_amounts[i] > 1:
            print(f"{uk_coins_amounts[i]} {uk_coins[i]} coins, ", end = "")
        elif uk_coins_amounts[i] == 1:
            print(f"{uk_coins_amounts[i]} {uk_coins[i]} coin, ", end = "")
    if uk_coins_amounts[-1] == 0:
        print("and you'll have no pennies left over!")
    else:
        if uk_coins_amounts[-1] != 1:
            print(f"and you'll have {uk_coins_amounts[-1]} pennies left over!")
        else:
            print(f"and you'll have {uk_coins_amounts[-1]} penny left over!")
    print(f"In US Dollars that is {pennies_converted_to_USD}")
    print(f"In Malagasy Ariary that is {pennies_converted_to_MGA}")
#main program starts here

def main():
    #print configuration first
    print("Here is the current configuration of the program: ")
    print(CONFIG)
    print("\n")
    
    sorter_choice = input("Please select 1 for the single coin sorter, 2 for the multiple coin sorter, or 3 for currency conversion.")
    #Used for if invalid input entered
    valid =['1', '2', '3']
    while sorter_choice != valid:

        if sorter_choice == '1':
            
            pennies = get_penny_amount()
            while pennies < 0:
                pennies = get_penny_amount()
            denomination = get_denomination()          
            while denomination == "incorrect_usage":
                denomination = get_denomination()
            coin_exchange(pennies, denomination)

            #simplest way to repeat program
            repeat1 = input("Would you like to sort more pennies? Press n for no, or any key for yes.")
            
            if repeat1 == 'n':
                break
            
        if sorter_choice == '2':
            pennies = get_penny_amount()
            while pennies < 0:
                pennies = get_penny_amount()
            excluded_denomination = exclude_denomination()
            while excluded_denomination == "incorrect_usage":
                excluded_denomination = exclude_denomination()
            uk_coins_amounts = calculate(pennies, excluded_denomination)
            result_print(uk_coins, uk_coins_amounts, pennies)

            repeat1 = input("Would you like to sort more pennies? Press n for no, or any key for yes.")
            if repeat1 == 'n':
                break

        if sorter_choice == '3':
            pounds = get_pounds_amount()
            #gets user to input a different amount if they have entered an incorrect amount
            while pounds == 0:
                pounds = get_pounds_amount()
            #converts pounds to USD or MGA if pound amount is between 0.01 and 100.00 inclusive
            GBPUSD = Get_Currency_Rates()['GBP_USD']
            GBPMGA = Get_Currency_Rates()['GBP_MGA']
            pounds_converted_to_USD = round(pounds * GBPUSD, 2)
            pounds_converted_to_MGA = round(pounds * GBPMGA, 2)
            #print "{:12.2f}".format(x)
            print(f"The amount was {pounds} in Pounds Sterling.")
            print(f"In US Dollars that is {pounds_converted_to_USD}")
            print(f"In Malagasy Ariary that is {pounds_converted_to_MGA}")

            repeat1 = input("Would you like to run the program again? Press n for no, or any key for yes.")
            if repeat1 == 'n':
                break

        sorter_choice = input("Please select 1 for the single coin sorter, 2 for the multiple coin sorter, or 3 for currency conversion.")

main()