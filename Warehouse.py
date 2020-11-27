class Warehouse:
    def __init__(self):
        self._manufacturers = dict()
        self._size = dict()
        self._id = 0
        self._sneakers = dict()

    def add(self, sneakers):
        for sneaker in sneakers:
            self._sneakers[self._id] = sneaker

            if sneaker.manufacturer in self._manufacturers.keys():
                self._manufacturers[sneaker.manufacturer].append(self._id)
            else:
                self._manufacturers[sneaker.manufacturer] = list()
                self._manufacturers[sneaker.manufacturer].append(self._id)

            if sneaker.size in self._size:
                self._size[sneaker.size].append(self._id)
            else:
                self._size[sneaker.size] = list()
                self._size[sneaker.size].append(self._id)
            self._id += 1

    def remove(self, sneakers):
        if sneakers is not None:
            for i in self._sneakers.keys():
                if self._sneakers[i] == sneakers:
                    self._sneakers.pop(i, None)

    def displayAllSneakers(self):
        print("Товары на складе:")
        for key, value in self._sneakers.items():
            print(f'id - {key};name - {value.name};count - {value.count}; '
                  f'manufacturer - {value.manufacturer}; price - {value.price}; size - {value.size};')

    def getStatByManufacturer(self):
        print('Производители:')
        for manufacturer in self._manufacturers.keys():
            print(f'{manufacturer}:\n\t')
            for sneaker in self._manufacturers[manufacturer]:
                print(f'id - {sneaker};\n\t'
                      f'Название: {self._sneakers[sneaker].name};\n\t'
                      f'Количество: {self._sneakers[sneaker].count};\n\t'
                      f'Цена: {self._sneakers[sneaker].price};\n\t'
                      f'Размер: {self._sneakers[sneaker].size};')

    def getStatBySize(self):
        print('Размеры:')
        for size in self._size.keys():
            print(f'{size}:\n\t')
            for sneaker in self._size[size]:
                print(f'id - {sneaker};\n\t'
                      f'Название - {self._sneakers[sneaker].name};\n\t'
                      f'Количество - {self._sneakers[sneaker].count};\n\t'
                      f'Производитель - {self._sneakers[sneaker].manufacturer};\n\t'
                      f'Цена - {self._sneakers[sneaker].price};\n\t')