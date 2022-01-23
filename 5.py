# Среди трех чисел найти среднее, Которое больше первого, но меньше второго

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if (c > a > b or b > a > c):
    print("Среднее: ", a)
elif (a > b > c or c > b > a):
    print("Среднее: ", b)
else:
    print("Среднее: ", c)