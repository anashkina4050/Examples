# Найти максимальное из трех целых чисел

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

m = a
if m < b:
    m = b
if m < c:
    m = c
print(m)