# variables for whole application
currency_config = {
    'currency' : 'GBP',
    'currency_major' : '£',
    'currency_minor' : 'p',
    'currency_word' : 'pence',

}
currency = 'GBP'
curr_symbol = '£'
min_input = 0
max_input = 10000
coins = ["£2", "£1","50p","20p","10p"]

'''
coins = [f'{currency_config["currency_major"]}2',
        f'{currency_config["currency_major"]}1',
        f'50{currency_config["currency_minor"]}',
        f'20{currency_config["currency_minor"]}',
        f'10{currency_config["currency_minor"]}']
'''

coins_value = [200,100,50,20,10]

# variables for single coin calculator
single_inputted_amount = -1
single_denomination = 200

# variables for multiple coin calculator
multi_inputted_amount = -2
multi_denomination = [200,100,50,20,10]
used_denomination = []
excluded_denomination = 200

# A useful list and dictionary for UK currency
uk_coins = ["£2", "£1", "50p", "20p", "10p"]
uk_coins_dict = {
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20,
        "10p": 10,
    }