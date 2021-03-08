
# ----- VARIABLES FOR WHOLE APPLICATION -----

# dictionary for  the currency that user is currently working in
# used mainly for output text
currency_config = {
    'currency' : 'GBP',
    'currency_major' : '£',
    'currency_minor' : 'p',
    'currency_word' : 'pence',
}

# minimum and maximum input
min_input = 0
max_input = 10000

# list of available coins as strings
# set to GBP or USD in configMenu
coins = ["£2", "£1","50p","20p","10p"]

# list of coin values in smallest denomination (so use 20p and 20c)
# THIS STAYS CONSTANT
coins_value = [200,100,50,20,10]

# initialised to -1 to check if a value has been inputted
# negative numbers cannot be inputted by user; so safe to use -1
single_inputted_amount = -1

# as dropdown box is in £2/$2 selection by default
single_denomination = 200



# ----- VARIABLES FOR MULTIPLE COIN CALCULATOR -----

# initialised to -2 to check if a value has been inputted
multi_inputted_amount = -2

# list of all available coins; only for the multi coin calculator
multi_denomination = [200,100,50,20,10]

# list of all coins with the excluded coin set to 0
# by default dropdown menu set at 200, so initialised to remove 200
missing_denom = [0,100,50,20,10]

# stores the amount of the excluded coin (can be 200, 100, 50, 20, 10)
excluded_denomination = 200

# list to store how many of each coin the user can get
# one should always be 0; the excluded one
# index place related to multi_denomination/ coins_value e.g. [200,100,50,20,10]
how_many_of_each = [0,0,0,0,0]

