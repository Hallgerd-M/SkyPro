from typing import List, Dict

def filter_by_state(my_dictionary: List[Dict], state: str) -> List[Dict]:
    """принимает список словарей и возвращает новый список по значению ключа state"""
    filtered_dictionary = []
    for dictionary in my_dictionary:
        if dictionary.get('state') == state.upper():
            filtered_dictionary.append(dictionary)
    return filtered_dictionary


def sort_by_date(my_dictionary: List[Dict], reverse: bool = True) -> List[Dict]:
    """сортирует принимаемый список по дате"""
    if reverse is True:
        sorted_dictionary = sorted(my_dictionary, key=lambda item: item["date"])
        return sorted_dictionary
    else:
        sorted_dictionary = sorted(
            my_dictionary, key=lambda item: item["date"], reverse=True
        )
        return sorted_dictionary


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
    print(
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )


"""    assert sort_by_date(my_dictionary) == [{
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                }]"""
