import os
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите Имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное Имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите Фамилию: ")
            if len(last_name) < 2:
                raise NameError("Не валидная Фамилия")
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err)

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер телефона: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера телефона")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер телефона!!!")
        except LenNumberError as err:
            print(err)

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy_entry(source_file, destination_file):
    try:
        entry_number = int(input("Введите номер строки для копирования: ")) - 1
        source_data = read_file(source_file)

        if 0 <= entry_number < len(source_data):
            entry_to_copy = source_data[entry_number]
            write_file(destination_file, [entry_to_copy["Имя"], entry_to_copy["Фамилия"], entry_to_copy["Телефон"]])
            print("Данные успешно скопированы.")
        else:
            print("Неверный номер строки.")

    except ValueError:
        print("Введите корректный номер строки.")

def display_data(file_name):
    data = read_file(file_name)
    if not data:
        print("Телефонная книга пуста.")
    else:
        print(f"{'Имя':<15}{'Фамилия':<15}{'Телефон':<15}")
        print("-" * 45)
        for row in data:
            print(f"{row['Имя']:<15}{row['Фамилия']:<15}{row['Телефон']:<15}")

def main():
    file_name = 'phone.csv'
    while True:
        print("Выберите команду:")
        print("1. Вывести данные")
        print("2. Сохранить данные")
        print("3. Поиск по характеристике")
        print("4. Копировать данные из одного файла в другой")
        print("q. Выйти")

        command = input("Введите номер команды: ")

        if command == '1':
            if not os.path.exists(file_name):
                print("Файл отсутствует. Создайте его")
            else:
                display_data(file_name)
        elif command == '2':
            if not os.path.exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == '3':
            pass
        elif command == '4':
            source_file = input("Введите имя файла, из которого нужно скопировать данные: ")
            destination_file = input("Введите имя файла, в который нужно скопировать данные: ")

            if os.path.exists(source_file) and os.path.exists(destination_file):
                copy_entry(source_file, destination_file)
            else:
                print("Один из файлов не существует. Убедитесь, что оба файла существуют.")
        elif command.lower() == 'q':
            break
        else:
            print("Некорректная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
