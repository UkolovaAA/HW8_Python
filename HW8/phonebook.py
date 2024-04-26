import os
import sys

def add_new_user(name: str, phone:str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
 
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"\n{name} - {number}")

def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open("number.txt", "r", encoding="utf-8") as file:
        return file.read()

def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    Функция для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
    
    with open("number.txt", "r", encoding="utf-8") as source:
        with open("file.txt", "a", encoding="utf-8" ) as dest:
            list_1 = file1.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)
             
 
INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""
file = "number.txt"

file1 = "file.txt"


if file not in os.listdir():
    print("Указанное имя файла отсутствует")
    sys.exit()

if file1 not in os.listdir():
    print("Указанная строка отсутствует")
    sys.exit()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
        pass
    elif mode == 2:
        name = input("Введите Ваше имя:")
        number = input("Введите номер:")
        add_new_user(name, number, file)
        pass
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        data = input("Введите номер строки для копирования: ")
        add_new_user('file.txt', data)
        pass
    