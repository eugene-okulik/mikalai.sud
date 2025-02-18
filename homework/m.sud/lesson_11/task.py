class Book:
    material_pages = "paper"
    have_text = True

    def __init__(self, name_book, author, n_pages, reserved):
        self.name_book = name_book
        self.author = author
        self.n_pages = n_pages
        self.reserved = reserved

    def info(self):
        print("Название книги: " + self.name_book)
        print("Автор книги: " + self.author)
        print("Количество страниц в книге: " + str(self.n_pages))
        print("Статус резерва книги: " + str(self.reserved))


book1 = Book("Книга про речку", "Речной Ф.Г", 100, False)
book2 = Book("Книга про лес", "Лесной Т.В", 110, False)
book3 = Book("Книга про небо", "Небесный Ф.Л", 150, False)
book4 = Book("Книга про море", "Морской С.С", 200, False)
book5 = Book("Книга про дом", "Домашний А.А", 1200, True)

book1.info()
print()
print()
book2.info()
print()
print()


class SchoolBooks(Book):
    def __init__(self, name_book, author, n_pages, reserved, name_predmet, number_class, have_task):
        super().__init__(name_book, author, n_pages, reserved)
        self.name_predmet = name_predmet
        self.number_class = number_class
        self.have_task = have_task

    def info(self):
        super().info()
        print("Название предмета: " + self.name_predmet)
        print("Номер класса: " + str(self.number_class))
        print("Статус наличия заданий: " + str(self.have_task))


book6 = SchoolBooks("Алгебра для школьников", "Автор алгебры", 100, False, "Математика", 6, True)
book7 = SchoolBooks("Физика для школьников", "Автор физики", 150, True, "Физика", 9, False)

book7.info()
print()
print()
book6.info()
