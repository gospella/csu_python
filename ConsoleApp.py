from DB import LoadFile, InputSneakersInfo
from Warehouse import Warehouse

warehouse = Warehouse()
data = LoadFile('products.txt')
warehouse.add(data)


def PrintMenuStartInfo():
    print(f'Добро пожаловать в систему учета для складских остатков\n'
          f'Введите один из вариантов в меню и нажмите Enter\n'
          f'1. Добавить товар\n'
          f'2. Загрузить товары с файла\n'
          f'3. Удалить товар\n'
          f'2. Список всех товаров\n'
          f'4. Статистика по категориям\n')


while True:
    PrintMenuStartInfo()
    option = int(input())
    if option == 1:
        sneakers = list()
        sneakers.append(InputSneakersInfo())
        warehouse.add(sneakers)
    elif option == 2:
        data = LoadFile('products.txt')
        warehouse.add(data)
    elif option == 3:
        warehouse.displayAllSneakers()
        sneakers = InputSneakersInfo()
        warehouse.remove(sneakers)
    elif option == 4:
        warehouse.displayAllSneakers()
    elif option == 5:
        warehouse.getStatByManufacturer()
    elif option == 6:
        warehouse.getStatBySize()

