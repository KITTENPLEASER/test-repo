import requests as req

BASE_URL = "https://api.exchangerate-api.com/v4/latest/USD"
GET_REQUEST = req.get(BASE_URL).json()

def get_rate(currency: str) -> float:
    return GET_REQUEST['rates'][f'{currency}']

print(get_rate('RUB'))