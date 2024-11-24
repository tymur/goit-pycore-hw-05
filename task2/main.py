import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генерує всі дійсні числа з тексту.
    
    Параметри:
    text (str): Вхідний текст.

    Повертає:
    Генератор чисел (float) з тексту.
    """
    # Використовуємо регулярний вираз для знаходження чисел
    for match in re.finditer(r'\b\d+\.\d+|\b\d+\b', text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    """
    Обчислює загальну суму чисел у тексті, використовуючи задану функцію генератора.

    Параметри:
    text (str): Вхідний текст.
    func (Callable): Функція-генератор.

    Повертає:
    float: Загальна сума чисел у тексті.
    """
    return sum(func(text))


# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1500.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
