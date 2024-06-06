from typing import Union

def mask_account_card(card_or_account_info: str) -> str:
    """принимает название и номер карты или номер счета и возвращает замаскированный номер"""
    card_info = []
    account_info = []
    for letter in card_or_account_info:
        if letter == "С":
            account_info.append(card_or_account_info[:4])
            account_number = int(card_or_account_info[5:])
            mask_account_number = get_mask_account(account_number)
            account_info.append(mask_account_number)
            mask_account_info = " ".join(account_info)
    return mask_account_info

