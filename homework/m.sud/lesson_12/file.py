# +Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# +Создать экземпляры (объекты) цветов разных видов.
# +Собрать букет (букет - еще один класс) с определением его стоимости.
# +В букете цветы пусть хранятся в списке. Это будет список объектов.

# +Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов
# +в букете.

# +Позволить сортировку цветов в букете на основе различных параметров
# +(свежесть/цвет/длина стебля/стоимость)(это тоже методы)

# +Реализовать поиск цветов в букете по каким-нибудь параметрам
# +(например, по среднему времени жизни) (и это тоже метод).

class Flawors:
    its_flawor = True


class Market(Flawors):
    def __init__(self, name, price, time, color, size):
        self.name = name
        self.price = price
        self.time = time
        self.color = color
        self.size = size

    def __repr__(self):
        return f'{self.name})'


class RedFlawors(Market):
    def __init__(self, name, price, time, color, size):
        super().__init__(name, price, time, color, size)


class BlueFlawors(Market):
    def __init__(self, name, price, time, color, size):
        super().__init__(name, price, time, color, size)


fl1 = RedFlawors("fl_red_1", 10, 10, "red", 140)
fl2 = RedFlawors("fl_red_2", 11, 11, "red", 100)
fl3 = BlueFlawors("fl_blue_1", 5, 5, "blue", 800)
fl4 = BlueFlawors("fl_blue_2", 6, 6, "blue", 4)


class Stack:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def st_price(self):
        return sum(flower.price for flower in self.flowers)

    def time_live(self):
        return sum(flower.time for flower in self.flowers) / len(self.flowers)

    def sort_by_price(self):
        return sorted(self.flowers, key=lambda flower: flower.price, reverse=True)

    def sort_by_color(self):
        return sorted(self.flowers, key=lambda flower: flower.color, reverse=True)

    def sort_by_size(self):
        return sorted(self.flowers, key=lambda flower: flower.size, reverse=True)

    def search(self, **kwargs):
        results = self.flowers
        for key, value in kwargs.items():
            if key == "price":
                results = [flower for flower in results if flower.price == value]
            elif key == "time":
                results = [flower for flower in results if flower.time == value]
            elif key == "color":
                results = [flower for flower in results if flower.color == value]
        return results


stak1 = Stack()
stak1.add_flower(fl1)
stak1.add_flower(fl2)

stak2 = Stack()
stak2.add_flower(fl1)
stak2.add_flower(fl2)
stak2.add_flower(fl3)
stak2.add_flower(fl4)

all_stak = [stak1, stak2]

print(f'Стоимость букета: {stak1.st_price()}; Срок увядания: {stak1.time_live()} дней; Cостав: {stak1.flowers}.')
print(f'Стоимость букета: {stak2.st_price()}; Срок увядания: {stak2.time_live()} дней; Cостав: {stak2.flowers}.')

print(stak1.sort_by_price())
print(stak2.sort_by_price())

print(stak1.sort_by_color())
print(stak2.sort_by_color())

print(stak1.sort_by_size())
print(stak2.sort_by_size())

sort_staks = sorted(all_stak, key=lambda stak: stak.st_price(), reverse=True)
for stak in sort_staks:
    print(f'Букет с ценой {stak.st_price()} и составом {stak.flowers}.')

print()
print(stak1.search(price=10))
