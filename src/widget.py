


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
        elif letter == "M" or letter == "V":
            card_info.append(card_or_account_info[:-17])
            card_number = int(card_or_account_info[-16:])
            mask_card_number = get_mask_card_number(card_number)
            card_info.append(mask_card_number)
            mask_card_info = " ".join(card_info)
            return mask_card_info


def get_data(date_info: str) -> str:
    date_data = []
    date_data.extend([date_info[8:10], date_info[5:7], date_info[:4]])
    new_date_data = ".".join(date_data)
    return new_date_data

