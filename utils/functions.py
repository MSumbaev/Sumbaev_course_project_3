import json

PATH = "/home/msumbaev/PycharmProjects/Sumbaev_course_project_3/data/operations.json"


def load_data(path):
    """Возвращает информацию из фа йла.json.
    :param path - путь к файлу.json.
    """
    with open(path) as file:
        data = json.load(file)
        return data


def get_sort_executed_operations(operations, number_of_operations=5):
    """Возвращает количество последних выполненных операций
    :param operations - список всех операций.
    :param number_of_operations - количество последних операций (по умолчанию 5).
    """
    # operations_executed = [operation for operation in operations if operation["state"] == "EXECUTED"]
    operations_executed = []

    for op in operations:

        if op.get("state", False) and op["state"] == "EXECUTED":
            operations_executed.append(op)

    sorted_operations_executed = sorted(operations_executed, reverse=True, key=lambda d: d["date"])
    last_operations = [sorted_operations_executed[i] for i in range(number_of_operations)]
    return last_operations


def print_operations(operations):
    """Выводит на экран операции в формате:

    'Пример вывода для одной операции:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.'
    """
    pass
