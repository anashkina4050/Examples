# Определить кол-во четных и нечетных цифр в указанном числе

a = int(input("Многозначное целое число: "))
even = 0
odd = 0

while a > 0:
    if a % 2 ==0:
        even += 1
    else:
        odd += 1
    a = a // 10
print("Четных цифр: ", even)
print("Нечетных цифр: ", odd)