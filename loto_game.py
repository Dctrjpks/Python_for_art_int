import random
import os
import sys

max_num = 90
all_numbers = []
for j in range(1,91):
    all_numbers.append(j)
num_per_card = 15

def make_row(): # делает в ИНТАХ 1й ряд карты
    nums_per_line = 0
    while nums_per_line != 5:
        factor = [random.randint(0, 1) for i in range(9)]
        nums_per_line = sum(factor)
    row = [factor[i]*(random.randint(1, 9)+10 * i)for i in range(9)]
    return row
def make_row2(row1): # делает в ИНТАХ 2й ряд карты без повторов
    row_comp = list(set(row1) & set(row1))
    while len(row_comp) > 1:
        row2 = make_row()
        row_comp = list(set(row1) & set(row2))
    return row2
def make_row3(row1, row2): # делает в ИНТАХ третий ряд карты без пустых и полных колонок.
    spec = []
    row3 = [0] * 9
    row_comp2 = list(set(row2) & set(row2))
    while len(row_comp2) > 1:
        for i in range(9):
            if row1[i] == 0 and row2[i] == 0:
                row3[i] = (random.randint(1, 9)+10 * i)
                spec.append(i)
            if row1[i] != 0 and row2[i] != 0:
                row3[i] = 0
                spec.append(i)
            else:
                row3[i] = (random.randint(1, 9)+10 * i)
            i+=1
        row_comp2 = list(set(row2) & set(row3))
        # print(spec)
        # if row3.count(0) > 4:
        #     pass
    return row3
def make_card():
    card = []
    row1 = make_row()
    row2 = make_row2(row1)
    # y = 0
    # while y != 4:
    row3 = make_row3(row1, row2)
    # y = row3.count(0)
    out_row1 = []
    out_row2 = []
    out_row3 = []
    for ii in range(9): # переводим карты в СТРИНГИ
        out_row1.append(str(row1[ii]))
        out_row2.append(str(row2[ii]))
        out_row3.append(str(row3[ii]))
    for iii in range(9):
        if out_row1[iii] == '0':
            out_row1[iii] = '  '

        if out_row2[iii] == '0':
            out_row2[iii] = '  '

        if out_row3[iii] == '0':
            out_row3[iii] = '  '

    if out_row1[0] != '  ':
        out_row1[0] = ' '+out_row1[0]
    if out_row2[0] != '  ':
        out_row2[0] = ' '+out_row2[0]
    if out_row3[0] != '  ':
        out_row3[0] = ' '+out_row3[0]
    card.append(out_row1)
    card.append(out_row2)
    card.append(out_row3)
    return card
def print_card(card, name): # выводит карту в консоль
        print('{:-^27}'.format(name))
        for i4 in range(3):
            print(' '.join(card[i4]))
# делаем карты

player_card = make_card()
computer_card = make_card()

print_card(player_card, 'Карточка игрока ')
print_card(computer_card, 'Карточка компьютера ')

# делаем бочонки

barrels = []
for i6 in range(1,91):
    barrels.append(i6)

# конец подготовки
# начало игры



barrel = barrels.pop(random.randint(1,len(barrels)-1))
print()
print('Выпал бочонок: ', barrel)
ping = input('Вычеркнуть номер? (y/n): ')
barrel = input('input test barrel: ')

if ping == 'y':
    if barrel not in player_card[0]+player_card[1]+player_card[2]:
        print('Вы проиграли! Внимательнее :-)')

for i7 in range(3):
    if barrel in player_card[i7]:
        place = player_card[i7].index(barrel)
        player_card[i7][place] = '><'
print_card(player_card, 'Карточка игрока ')

for i8 in range(3):
    if barrel in computer_card[i8]:
        place = computer_card[i8].index(barrel)
        computer_card[i8][place] = '><'
print_card(computer_card, 'Карточка компьютера ')

if ping == 'n':
    if barrel  in player_card[0]+player_card[1]+player_card[2]:
        print('Вы проиграли! Внимательнее :-)')








    # print('YES')
# print(player_card)
# print(computer_card)
# print('{:-^27}'.format(' Карточка игрока '))
# for i4 in range(3):
#     print(' '.join(player_card[i4]))
#
# print('{:-^27}'.format(' Карточка компьютера '))
# for i4 in range(3):
#     print(' '.join(computer_card[i4]))


