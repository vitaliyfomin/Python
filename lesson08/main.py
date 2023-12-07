from os.path import exists
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
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)

    last_name = "Иванов"

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
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

def main():
    file_name = 'phone.csv'
    while True:
        print("Выберите команду:")
        print("1. Вывести данные")
        print("2. Сохранить данные")
        print("3. Поиск по характеристике")
        print("q. Выйти")

        command = input("Введите номер команды: ")

        if command == '1':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
            else:
                print(*read_file(file_name))
        elif command == '2':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == '3':
            pass
        elif command.lower() == 'q':
            break
        else:
            print("Некорректная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
