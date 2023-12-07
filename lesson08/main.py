import os
from csv import DictReader, DictWriter

def copy_entry(source_file, destination_file):
    try:
        entry_number = int(input("Введите номер строки для копирования: ")) - 1  # Строки начинаются с 1, а индексы с 0
        source_data = read_file(source_file)

        if 0 <= entry_number < len(source_data):
            entry_to_copy = source_data[entry_number]
            write_file(destination_file, [entry_to_copy["Имя"], entry_to_copy["Фамилия"], entry_to_copy["Телефон"]])
            print("Данные успешно скопированы.")
        else:
            print("Неверный номер строки.")

    except ValueError:
        print("Введите корректный номер строки.")

def main():
    file_name = 'phone02.csv'
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
                print(*read_file(file_name))
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