


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b


def main():
    print("=== Калькулятор ===")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'exit'")

    while True:
        user_input = input("\nВведите пример (например: 5 + 3) или 'exit': ")

        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Ошибка: введите данные в формате '5 + 3'")
                continue

            num1 = float(parts[0])
            sign = parts[1]
            num2 = float(parts[2])

            if sign == '+':
                result = add(num1, num2)
            elif sign == '-':
                result = subtract(num1, num2)
            elif sign == '*':
                result = multiply(num1, num2)
            elif sign == '/':
                result = divide(num1, num2)
            else:
                print("Ошибка: неизвестный знак операции")
                continue

            print(f"Результат: {result}")

        except ValueError:
            print("Ошибка: проверьте, что вы ввели числа.")


if __name__ == "__main__":
    main()