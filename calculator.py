"""
Модуль калькулятора с историей операций
"""
from datetime import datetime


class CalculatorHistory:
    """Класс для хранения истории операций"""

    def __init__(self):
        """Инициализация пустой истории"""
        self.history = []

    def add_operation(self, operation, num1, num2, result):
        """
        Добавить операцию в историю

        Args:
            operation (str): знак операции (+, -, *, /)
            num1 (float): первое число
            num2 (float): второе число
            result (float): результат
        """
        record = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'operation': operation,
            'num1': num1,
            'num2': num2,
            'result': result
        }
        self.history.append(record)

    def get_history(self):
        """Получить всю историю операций"""
        return self.history

    def clear_history(self):
        """Очистить историю"""
        self.history = []

    def show_history(self):
        """Отобразить историю в читаемом виде"""
        if not self.history:
            return "История пуста"

        output = "\n=== ИСТОРИЯ ОПЕРАЦИЙ ===\n"
        for record in self.history:
            output += f"[{record['timestamp']}] {record['num1']} {record['operation']} {record['num2']} = {record['result']}\n"
        return output


class Calculator:
    """Калькулятор с историей операций"""

    def __init__(self):
        """Создать калькулятор с пустой историей"""
        self.history = CalculatorHistory()

    def add(self, a, b):
        """Сложение с записью в историю"""
        result = a + b
        self.history.add_operation('+', a, b, result)
        return result

    def subtract(self, a, b):
        """Вычитание с записью в историю"""
        result = a - b
        self.history.add_operation('-', a, b, result)
        return result

    def multiply(self, a, b):
        """Умножение с записью в историю"""
        result = a * b
        self.history.add_operation('*', a, b, result)
        return result

    def divide(self, a, b):
        """Деление с записью в историю"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно!")
        result = a / b
        self.history.add_operation('/', a, b, result)
        return result

    def show_history(self):
        """Показать историю операций"""
        return self.history.show_history()

    def clear_history(self):
        """Очистить историю операций"""
        self.history.clear_history()