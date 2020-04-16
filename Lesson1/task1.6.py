#6.Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

while True:
    user_a = input("Введите результат за первый день в км:\n")
    if user_a.isdigit():
        user_a = int(user_a)
        break
    else:
        print("Ошибка ввода, это не число")

while True:
    user_b = input("Введите общий результат в км:\n")
    if user_b.isdigit():
        b = int(user_b)
        break
    else:
        print("Ошибка ввода, это не число")
day = 1
while int(user_a) < int(user_b):
    user_a = user_a + (user_a * 0.1)
    day += 1
print(f"Вы достигнете требуемых показателей на %d день" % day)