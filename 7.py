# Угадай число

import random
num = random.randint(1, 100)
while True:
    print("Угадайте число от 1 до 100")
    guess = int(input())
    if guess == num:
        print("Правильно!")
        break
    elif guess < num:
        print("Загаданное число больше")
    elif guess > num:
        print("Загаданное число меньше")