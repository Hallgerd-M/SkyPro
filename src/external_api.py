import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency: str) -> Any:
    """Функция принимает значение в долларах или евро, обращается к API и возвращает конвертацию в рубли"""
    if currency == "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        json_result = response.text
        rub_amount = json.loads(json_result)["result"]
        return rub_amount
    elif currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        json_result = response.text
        rub_amount = json.loads(json_result)["result"]
        return rub_amount


# if __name__ == "__main__":
#    print(convert_to_rub(45, "USD"))
