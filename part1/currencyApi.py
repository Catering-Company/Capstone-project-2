# Module need for to request currency data. Module for working with json also.
import requests
import json

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



