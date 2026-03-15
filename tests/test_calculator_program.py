import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_subtraction():
    assert calculate(10, 4, '-') == 6

def test_calculate_multiplication():
    assert calculate(3, 5, '*') == 15

def test_calculate_division_by_zero():
    assert calculate(10, 0, '/') == "Ошибка: Деление на ноль."
def test_calculate_negative_numbers():
    assert calculate(-5, -3, '+') == -8
    assert calculate(-5, -3, '-') == -2
    assert calculate(-5, -3, '*') == 15
    assert calculate(-5, -3, '/') == 1.6666666666666667
'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
