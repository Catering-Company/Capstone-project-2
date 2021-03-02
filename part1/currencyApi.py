# Module need for to request currency data.
import requests

# Hidden Api key. Key is hidden for security
Api_key_file = open("./Apikey.txt", "r")
Api_key = Api_key_file.read()

# Get request for currency data. Request will return a JSON.
data = requests.get('http://api.currencylayer.com/live?access_key='+Api_key+'&currencies=GBP,MGA&format=1')

print(data.json())































