# Перевернуть число

N = int(input("Введите целое число - "))
n = 0

while N > 0:
    digit = N % 10
    N = N // 10
    n = n * 10
    n = n + digit
print("Результат - ", n)