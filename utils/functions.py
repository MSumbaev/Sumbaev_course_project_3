import json


PATH = "/home/msumbaev/PycharmProjects/Sumbaev_course_project_3/data/operations.json"


def load_data(path):
    """Возвращает информацию из фа йла.json.
    :param path - путь к файлу.json.
    """
    with open(path) as file:
        data_json = file.read()
        data = json.loads(data_json)
        return data


def get_sort_executed_operations(operations_list, number_of_operations=5):
    """Возвращает количество последних выполненных операций
    :param operations_list - список всех операций.
    :param number_of_operations - количество последних операций (по умолчанию 5).
    """
    pass


def print_operations(operations):
    """Выводит на экран операции в формате:

    'Пример вывода для одной операции:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.'
    """
    pass
