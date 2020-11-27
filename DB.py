#Пока без бд
from Sneackers import Sneakers

def InputSneakersInfo():
    print('Введите название кросовок:')
    name = input()
    print('Введите количество:')
    count = int(input())
    print('Введите производителя:\n')
    manufacturer = input()
    print('Введите цену:\n')
    price = float(input())
    print('Введите размер:\n')
    size = int(input())
    return Sneakers(name, count, manufacturer, price, size)

def LoadFile(filename):
    res_list = list()
    with open(filename) as file:
        data = file.read().split('\n')
    for d in data:
        row = d.split()
        res_list.append(Sneakers(row[0], row[1], row[2], row[3], row[4]))
    return  res_list