import random

def main_menu():
    while True:
        print("\n*   Таблиця множення   *")
        print("1. Перегляд")
        print("2. Тренування")
        print("3. Тести")
        print("4. Автор")
        print("5. Вихід")

        choice = input("Виберіть пункт меню (1-5): ")

        if choice == "1":
            view_table()
        elif choice == "2":
            training()
        elif choice == "3":
            tests()
        elif choice == "4":
            show_author()
        elif choice == "5":
            print("Програму завершено.")
            break
        else:
            print("Невірний вибір!")


def view_table():
    while True:
        print("\n*   Перегляд таблиці   *")
        print("1. Вся таблиця")
        print("2. Частина таблиці (по числу)")
        print("3. Назад")

        choice = input("Виберіть пункт меню (1-3): ")

        if choice == "1":
            for i in range(1, 10):
                line = ""
                for j in range(1, 10):
                    line += f"{i}×{j}={i*j}  "
                print(line.strip())
            input("\nНатисніть Enter для повернення...")
        elif choice == "2":
            try:
                num = int(input("Введіть число (1-9): "))
                if 1 <= num <= 9:
                    for j in range(1, 10):
                        print(f"{num}×{j}={num*j}")
                else:
                    print("Число повинно бути від 1 до 9!")
            except ValueError:
                print("Введіть числове значення!")
            input("\nНатисніть Enter для повернення...")
        elif choice == "3":
            break
        else:
            print("Невірний вибір!")


def training():
    while True:
        print("\n*   Тренування   *")
        print("1. Вся таблиця")
        print("2. Частина таблиці")
        print("3. Назад")

        choice = input("Виберіть пункт (1-3): ")

        if choice == "1":
            try:
                n = int(input("Скільки прикладів ви хочете потренувати? "))
                correct = 0
                for _ in range(n):
                    a = random.randint(1, 9)
                    b = random.randint(1, 9)
                    answer = input(f"{a}×{b} = ")
                    if answer.isdigit() and int(answer) == a*b:
                        print("✅ Правильно!")
                        correct += 1
                    else:
                        print(f"❌ Неправильно! Правильна відповідь: {a*b}")
                print(f"\nТренування завершено! Результат: {correct}/{n}")
            except ValueError:
                print("Введіть числове значення!")
        elif choice == "2":
            try:
                num = int(input("Введіть число для тренування (1-9): "))
                if 1 <= num <= 9:
                    tasks = list(range(1, 10))
                    random.shuffle(tasks)
                    correct = 0
                    for b in tasks:
                        answer = input(f"{num}×{b} = ")
                        if answer.isdigit() and int(answer) == num*b:
                            print("✅ Правильно!")
                            correct += 1
                        else:
                            print(f"❌ Неправильно! Правильна відповідь: {num*b}")
                    print(f"\nТренування завершено! Результат: {correct}/9")
                else:
                    print("Число повинно бути від 1 до 9!")
            except ValueError:
                print("Введіть числове значення!")
        elif choice == "3":
            break
        else:
            print("Невірний вибір!")


def tests():
    while True:
        print("\n*   Тести   *")
        print("1. 10 питань")
        print("2. 20 питань")
        print("3. Назад")

        choice = input("Виберіть пункт меню (1-3): ")

        if choice == "1":
            run_test(10)
        elif choice == "2":
            run_test(20)
        elif choice == "3":
            break
        else:
            print("Невірний вибір!")


def run_test(count):
    results = []
    correct = 0
    for _ in range(count):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        answer = input(f"{a}×{b} = ")
        correct_ans = a * b
        if answer.isdigit() and int(answer) == correct_ans:
            results.append(f"{a}×{b} = {correct_ans}, ваш відповідь: {answer} ✅")
            correct += 1
        else:
            results.append(f"{a}×{b} = {correct_ans}, ваш відповідь: {answer} ❌")
    print(f"\nТест завершено! Результат: {correct} / {count}")
    print("\n".join(results))
    input("\nНатисніть Enter для повернення в меню...")


def show_author():
    print("\n *  Інформація про автора😎  *")
    print("Програму виконав: Тараканов Родіон Сергійович")
    print("Група: ПД-22")
    input("\nНатисніть Enter для повернення в меню...")


main_menu()
