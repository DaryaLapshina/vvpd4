"""дедлайн (результат лени)"""
import fnmatch
from datetime import date


def check_data(data):
    if fnmatch.fnmatch(data, '??.??.????') and \
            (''.join(data.split('.'))).isnumeric():
        day, month, year = [int(i) for i in data.split('.')]
        if ((month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32) or
                (month in [4, 6, 9, 11] and 0 < day < 31) or
                (month == 2 and 0 < day < 29)):
            return date(year, month, day)

        else:
            return "Wrong"
    else:
        return "Wrong"


def convertor(arr):
    keys = [arr[i].split(':')[0] for i in range(len(arr))]
    values = [arr[i].split(':')[1] for i in range(len(arr))]
    dictionary = dict(zip(keys, values))
    return dictionary


def deadline_score(pass_date, deadline_date):
    pass_date = check_data(pass_date)
    deadline_date = check_data(deadline_date)
    print(pass_date)
    if pass_date == "Wrong" or deadline_date == "Wrong":
        return "Введённые данные неверны. Формат ввода: DD.MM.YYYY"
    else:
        if deadline_date >= pass_date:
            days = (deadline_date - pass_date).days
        else:
            days = (pass_date - deadline_date).days * (-1)
        if days >= 0:
            return 5
        elif -28 <= days < 0:
            days = days * (-1)
            for i in range(1, 5):
                if (i - 1) * 7 < days <= i * 7:
                    return 5 - i
        else:
            return 0


def late_list(grades, deadline_date):
    latecomers = []
    stu_del = []
    for key, value in grades.items():
        if check_data(value) == "Wrong":
            stu_del.append(key)
            print(key, "будет удалён из-за неверной даты")
    for i in stu_del:
        grades.pop(i)
    if check_data(deadline_date) == "Wrong":
        return "Введённые данные неверны. Формат ввода: DD.MM.YYYY"
    else:
        for key, value in grades.items():
            if deadline_score(value, deadline_date) < 5:
                latecomers.append(key)
        return latecomers


def main():
    """Функция для загрузки данных из файла"""

    while True:

        answ = input("\n1. дата сдачи и дедлайн"
                     "\n2. список и дедлайн"
                     "\n3. Выход"
                     "\nВаше действие: ")

        match answ:
            case '1':
                data = input('Дата сдачи: ')
                deadline = input('Дата дедлайна: ')
                print(deadline_score(data, deadline))
            case '2':
                student = input("Словарь (Имя:дата сдачи): ").split(" ")
                a = convertor(student)
                deadline = input('Дата дедлайна: ')
                print(late_list(a, deadline))

            case '3':
                print("Программа завершена.")
                break

            case _:
                print("Неверно выбранное действие.")


main()
