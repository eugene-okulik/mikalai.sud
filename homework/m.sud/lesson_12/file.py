class Flawors:
    its_flawor = True

    def __init__(self, f_size, time_live, name, color):
        self.f_size = f_size
        self.time_live = time_live
        self.name = name
        self.color = color


class Market(Flawors):
    def __init__(self, fl_id, f_size, time_live, name, color, price):
        super().__init__(f_size, time_live, name, color)
        self.price = price
        self.fl_id = fl_id

    def __repr__(self):
        return f'{self.name})'


class FlRose(Market):
    def __init__(self, fl_id, f_size, time_live, name, color, price, spikes):
        super().__init__(fl_id, f_size, time_live, name, color, price, )
        self.fl_id = fl_id
        self.spikes = spikes


class FlRomashka(Market):
    def __init__(self, fl_id, f_size, time_live, name, color, price, dust):
        super().__init__(fl_id, f_size, time_live, name, color, price)
        self.dust = dust


fl1 = FlRose(101, 100, 10, "Белая роза", "white", 10, True)
fl2 = FlRose(102, 40, 15, "Роза красная с шипами", "red", 11, True)
fl3 = FlRomashka(201, 15, 20, "Ромашка обыкновенная", "white", 10, True)
fl4 = FlRomashka(202, 15, 20, "Ромашка луговая", "white-yellow", 11, False)


class Stack:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def st_price(self):
        return sum(flower.price for flower in self.flowers)

    def time_live(self):
        return sum(flower.time_live for flower in self.flowers) / len(self.flowers)

    def sort_by_price(self):
        print(f'Сортировка по цене: {sorted(self.flowers, key=lambda flower: flower.price, reverse=True)}')
        return sorted(self.flowers, key=lambda flower: flower.price, reverse=True)

    def buk_info(self):
        print(f'Стоимость букета: {self.st_price()}; Срок увядания: {self.time_live()} дней; Cостав: {self.flowers}.')

    def sort_by_color(self):
        print(f'Сортировка по цвету: {sorted(self.flowers, key=lambda flower: flower.color, reverse=True)}')
        return sorted(self.flowers, key=lambda flower: flower.color, reverse=True)

    def sort_by_size(self):
        print(f'Сортировка по размеру: {sorted(self.flowers, key=lambda flower: flower.f_size, reverse=True)}')
        return sorted(self.flowers, key=lambda flower: flower.f_size, reverse=True)

    def search(self, **kwargs):
        results = self.flowers
        for key, value in kwargs.items():
            if key == "price":
                results = [flower for flower in results if flower.price == value]
            elif key == "time":
                results = [flower for flower in results if flower.time_live == value]
            elif key == "color":
                results = [flower for flower in results if flower.color == value]
        return results


# решил сортировку по букетам реализовать как функцию, а не как метод
def sort_stak(all_stak):
    sort_staks = sorted(all_stak, key=lambda market: market.st_price(), reverse=True)
    for stak in sort_staks:
        print(f'Букет с ценой {stak.st_price()}.')


stak1 = Stack()
stak1.add_flower(fl1)
stak1.add_flower(fl2)

stak2 = Stack()
stak2.add_flower(fl1)
stak2.add_flower(fl2)
stak2.add_flower(fl3)
stak2.add_flower(fl4)

full_stak1 = [stak1, stak2]
full_stak2 = [stak2, stak1, stak2, stak1]
print()
stak1.buk_info()
stak2.buk_info()
print()
stak1.sort_by_price()
stak2.sort_by_price()
print()
stak1.sort_by_color()
stak2.sort_by_color()
print()
stak1.sort_by_size()
stak2.sort_by_size()
print()
sort_stak(full_stak2)
print()
sort_stak(full_stak1)
print()
# поиск впринципе можно тоже как функцию, ну да ладно
print(stak1.search(price=10))
