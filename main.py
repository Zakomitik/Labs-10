# Учебный проект для лабораторной работы № 2 по Git
# Программа демонстрирует простое меню и функции.

def show_greeting():
    print("Привет! Это учебный проект для лабораторной работы по Git.")


def show_student_b_feature():
    print("Функция Student B: изменение успешно добавлено.")


def main():
    show_greeting()

    print("\n1. Показать функцию Student B")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_student_b_feature()
    else:
        print("Выход из программы.")


if __name__ == "__main__":
    main()
