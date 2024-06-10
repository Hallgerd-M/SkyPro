from typing import Dict

def filter_by_state(my_dictionary: dict, state: str) -> dict:
    """принимает список словарей и возвращает новый список по значению ключа state"""
    new_dictionary = []
    for item in my_dictionary:
        if item['state'] == state:
            new_dictionary.append(item)
    return new_dictionary


def sort_by_date():
    pass

if __name__ == "__main__":
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'EXECUTED'))