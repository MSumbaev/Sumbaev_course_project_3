import json


def load_data(path):
    """Возвращает информацию из фа йла.json.
    :param path - путь к файлу.json.
    """
    with open(path) as file:
        data = json.load(file)
        return data


def get_last_executed_operations(operations, number_of_operations=5):
    """Возвращает количество последних выполненных операций
    :param operations - список всех операций.
    :param number_of_operations - количество последних операций (по умолчанию 5).
    """
    # operations_executed = [operation for operation in operations if operation["state"] == "EXECUTED"]

    operations_executed = []

    for operation in operations:

        if operation.get("state", False) and operation["state"] == "EXECUTED":
            operations_executed.append(operation)

    sorted_operations_executed = sorted(operations_executed, reverse=True, key=lambda d: d["date"])
    last_operations = [sorted_operations_executed[i] for i in range(number_of_operations)]
    return last_operations


def get_format_date(operation):
    """Возвращает дату операции в виде: 'число.месяц.год'."""

    date_list = operation["date"].split("T")[0].split("-")
    format_date = ".".join(date_list[::-1])
    return format_date


def get_description(operation):
    """Возвращает описание операции."""

    return operation["description"]


def get_formatted_bank_accounts(operation):
    """Возвращает форматированную строку о счетах банковской операции.

    При выполнении перевода возвращает строку в виде:
    Счет / Платежная система XXXX XX** **** XXXX -> Счет **XXXX

    При открытии счета возвращает номер счета в виде:
    Счет **XXXX
    """
    to_bank_account = operation["to"].split()
    format_to_bank_account = to_bank_account[0] + " **" + to_bank_account[1][-4:]

    if operation.get("from", False):

        from_ = operation["from"].split()
        payment_system = ' '.join(from_[:-1])
        card_num_list = list(from_[-1])
        len_card_num = len(card_num_list)
        card_num_list[-len_card_num + 6:-4] = ["*"] * (len_card_num - 10)

        for i in range(4, len_card_num, 5):
            card_num_list.insert(i, " ")

        format_from = payment_system + " " + "".join(card_num_list)

        return f"{format_from} -> {format_to_bank_account}"

    else:
        return format_to_bank_account


def get_operation_amount(operation):
    """Возвращает строку с суммой перевода и в какой валюте"""
    return f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}'


def get_formatted_operations(operations):
    """Возвращает список элементов, где каждый элемент содержит форматированную строку об операции.
    Пример вывода для одной операции:

        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб.

    """
    result = []

    for operation in operations:
        format_date = get_format_date(operation)
        description = get_description(operation)
        formatted_bank_accounts = get_formatted_bank_accounts(operation)
        operation_amount = get_operation_amount(operation)

        result.append(format_date + " " + description + "\n" + formatted_bank_accounts
                      + "\n" + operation_amount + "\n")

    return result
