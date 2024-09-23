API_KEY = "a917fbf7736bb721cef8f909a9d0516e-b97d2ebc31cbf4982fb5b722b621a63e"
ACCOUNT_ID = "101-011-20161521-001"
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'

#like Authorization header in postman
#f here is to let python know that there is a API key coming in {} 
SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}'
}