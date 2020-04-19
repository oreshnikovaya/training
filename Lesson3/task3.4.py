# 4.Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

#Первый способ
def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(2, -2))

#Второй способ
#Не понимаю, как тут использовать параметр b
def my_func_1(a, b):
    for i in range(a-1):
        a *= a
    return 1 / a
print(my_func_1(2, -2))


#Третий способ
def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result
print(my_func_2(2, -2))