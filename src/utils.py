import json
from typing import Any

from src.external_api import convert_to_rub


def get_transactions_dictionary(path: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data


def return_transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, если не в рублях, конвертирует в рубли"""
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                return transaction["operationAmount"]["amount"]
            else:
                not_rub_amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["code"]
                rub_amount = convert_to_rub(not_rub_amount, currency)
                return round(rub_amount, 2)


if __name__ == "__main__":
    transactions = get_transactions_dictionary("../data/operations.json")
    print(return_transaction_amount_in_rub(transactions, 142264268))
