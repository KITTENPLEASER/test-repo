import requests
import redis
import json
from fastapi import FastAPI

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

BASE_URL = "https://api.exchangerate-api.com/v4/latest"

@app.get("/convert")
def get_currency(amount: float, from_currency: str, to_currency: str):
    cached = r.get(f"rates:{from_currency}")
    if cached:
        rates = json.loads(cached)
    else:
        response = requests.get(f'{BASE_URL}/{from_currency}').json()
        rates = response['rates']
        r.setex(f'rates:{from_currency}', 3600, json.dumps(rates))
    result = rates[to_currency] * amount
    return {"from": from_currency, "to": to_currency, "result": result}
