from random import shuffle
from time import sleep

def draw(value):
    if 10 > value >= 6:
        print("     _______")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("____________")
    if value ==5:
        print("     _______")
        print("     |     |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("____________")
    if value ==4:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("           |")
        print("           |")
        print("           |")
        print("____________")
    if value == 3:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|\    |")
        print("           |")
        print("           |")
        print("____________")
    if value == 2:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|\    |")
        print("     |     |")
        print("           |")
        print("____________")
    if value == 1:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|\    |")
        print("     |     |")
        print("    /      |")
        print("____________")
    if value == 0:
        print("     _______")
        print("     |     |")
        print("     O     |")
        print("    /|\    |")
        print("     |     |")
        print("    / \    |")
        print("____________")
    print()

lives = 10
print(f"Привет, давай сыграем в виселицу! У тебя есть {lives} попыток!")

wordList = ["Урюпинск", "dota", "Python", "бор", "компьютер", "Вагнер"]

shuffle(wordList)
word = wordList.pop()
used = ""

while lives > 0:
    mistakes = 0
    for symb in word:
        if symb.lower() in used.lower():
            print(symb, end=" ")
        else:
            print('_', end=" ")
            mistakes += 1
    print("\n")

    if mistakes == 0:
        print("Ты выиграл!")
        break

    key = ""
    if len(key) < 1:
        print("\n")
        key = input("Введите букву: ")[0]
    if key in used:
        print("Эта буква уже была!")
    else:
        used += key

    if key.lower() not in word.lower():
        print("Неверно!")
        lives -= 1
        draw(lives)
        sleep(1)
        print(f"Жизней осталось: ", end=" ")
        for xd in range(lives):
            print("❤️", end=" ")
        print()
    if lives < 5:
        print("Подсказка: ", end=" ")
        if word == "Урюпинск":
            print("Город, в котором Андрей Соколов повстречал мальчика Ваню в произведении М.Шолохова <Судьба человека>")
        if word == "бор":
            print("Народное название соснового леса")
        if word == "Python":
            print("На каком языке программирования написана данная программа")
        if word == "Вагнер":
            print("Фамилия композитора музыкальной драмы <Полёт валькирий>")
        if word == "dota":
            print("Популярная онлайн-игра жанра MOBA разработанная компанией Valve")
        if word == "компьютер":
            print("Электронно-вычислительная машина, способная выполнять заданную последовательность операций, называемую программой")

    if lives == 0:
        print("\n\n\n\n\n\n\n\n\n\n\nТы проиграл!")
        break
    print("Используемые буквы: ", end=" ")
    for k in used:
        print(k, end=" ")
    print("\n")