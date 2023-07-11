from database import*

def main():
    file_tel = 'tel.txt'

    # Создает файл если его нет в папке
    with open("tel.txt", "a", ) as file:
        file.write("")

    while True:
        print('Выберите одно из действий:')
        print('1 — Вывести инфо на экран')
        print('2 — Произвести добавление данных')
        print('3 — Произвести изменение данных')
        print('4 — Произвести удаление данных')
        print('5 — Произвести поиск данных')
        print('6 - Сортировка имен по алфавиту')
        print('0 — Выход из программы')
        action = int(input('Действие: '))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        elif action == 5:
            found_data(file_tel)
        elif action ==6:
            sorted_data(file_tel)
        else:
            my_choice = 0
            print('До свидания')
            break

        
main()