from utils.functions import *

def main():
    # Записываем в константу путь к данным
    PATH = "/home/msumbaev/PycharmProjects/Sumbaev_course_project_3/data/operations.json"

    # записываем данные об операциях в переменную
    operations = load_data(PATH)

    # Записываем в переменную 5 (заданы по умолчанию вторым аргументом) последних выполненных операций
    required_operations = get_last_executed_operations(operations)

    # Записываем в переменную список строк
    # с отформатированной для вывода информацией по операциям
    result = get_formatted_operations(required_operations)

    # Выводим на экран результат
    for operation in result:
        print(operation)

main()
