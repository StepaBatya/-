a = input("Введите первое число в двоичной системе: ")
b = input("Введите второе число в двоичной системе: ")

a_dec = int(a, 2)
b_dec = int(b, 2)

summ = a_dec + b_dec

result = bin(summ)[2:]

print("Сумма в двоичной системе:", result)
10