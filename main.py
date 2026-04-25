
from calculator import Calculator


def main():
    """Основная функция калькулятора"""
    calc = Calculator()

    print("=== КАЛЬКУЛЯТОР С ИСТОРИЕЙ ===")
    print("Доступные операции: +, -, *, /")
    print("Команды:")
    print("  history - показать историю операций")
    print("  clear   - очистить историю")
    print("  exit    - выход из программы")
    print()

    while True:
        user_input = input("Введите операцию (например: 5 + 3): ")

        # Проверка на выход
        if user_input.lower() == 'exit':
            print("Спасибо за использование калькулятора. До свидания!")
            break

        # Показать историю
        if user_input.lower() == 'history':
            print(calc.show_history())
            continue

        # Очистить историю
        if user_input.lower() == 'clear':
            calc.clear_history()
            print("История очищена!")
            continue

        try:
            # Разбор ввода пользователя
            parts = user_input.split()

            if len(parts) != 3:
                print("❌ Ошибка: введите в формате 'число операция число'")
                print("   Пример: 10 + 5")
                continue

            # Преобразование к числам
            num1 = float(parts[0])
            operation = parts[1]
            num2 = float(parts[2])

            # Выполнение операции
            if operation == '+':
                result = calc.add(num1, num2)
            elif operation == '-':
                result = calc.subtract(num1, num2)
            elif operation == '*':
                result = calc.multiply(num1, num2)
            elif operation == '/':
                result = calc.divide(num1, num2)
            else:
                print(f"❌ Ошибка: неизвестная операция '{operation}'")
                print("   Доступные операции: +, -, *, /")
                continue

            print(f"✅ Результат: {result}")

        except ValueError as e:
            print(f"❌ Ошибка: {e}")
        except Exception as e:
            print(f"❌ Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()