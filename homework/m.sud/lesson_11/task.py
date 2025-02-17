class Book:
    material_pages = "paper"
    have_text = True

    def __init__(self, name_book, author, n_pages, reserved):
        self.name_book = name_book
        self.author = author
        self.n_pages = n_pages
        self.reserved = reserved


book1 = Book("Книга про речку", "Речной Ф.Г", 100, False)
book2 = Book("Книга про лес", "Лесной Т.В", 110, False)
book3 = Book("Книга про небо", "Небесный Ф.Л", 150, False)
book4 = Book("Книга про море", "Морской С.С", 200, False)
book5 = Book("Книга про дом", "Домашний А.А", 1200, True)

print("Название: " + book1.name_book + " Автор: " + book1.author + " Количество страниц: " + str(
    book1.n_pages) + " Зарезервирована: " + str(book1.reserved))
print("Название: " + book2.name_book + " Автор: " + book2.author + " Количество страниц: " + str(
    book2.n_pages) + " Зарезервирована: " + str(book2.reserved))
print("Название: " + book3.name_book + " Автор: " + book3.author + " Количество страниц: " + str(
    book3.n_pages) + " Зарезервирована: " + str(book3.reserved))
print("Название: " + book4.name_book + " Автор: " + book4.author + " Количество страниц: " + str(
    book4.n_pages) + " Зарезервирована: " + str(book4.reserved))
print("Название: " + book5.name_book + " Автор: " + book5.author + " Количество страниц: " + str(
    book5.n_pages) + " Зарезервирована: " + str(book5.reserved))


class SchoolBooks(Book):
    def __init__(self, name_book, author, n_pages, reserved, name_predmet, number_class, have_task):
        Book.__init__(self, name_book, author, n_pages, reserved)
        self.name_predmet = name_predmet
        self.number_class = number_class
        self.have_task = have_task


book6 = SchoolBooks("Алгебра для школьников", "Автор алгебры", 100, False, "Математика", 6, True)
book7 = SchoolBooks("Физика для школьников", "Автор физики", 150, True, "Физика", 9, False)

print("Название книги: " + book6.name_book + " Автор: " + book6.author + " Количество страниц:" + str(
    book6.n_pages) + " Зарезервирована: " + str(
    book6.reserved) + " Название предмета: " + book6.name_predmet + " Номер класса: " + str(
    book6.number_class) + " Имеются задания: " + str(book6.have_task))

print("Название книги: " + book7.name_book + " Автор: " + book7.author + " Количество страниц:" + str(
    book7.n_pages) + " Зарезервирована: " + str(
    book7.reserved) + " Название предмета: " + book7.name_predmet + " Номер класса: " + str(
    book7.number_class) + " Имеются задания: " + str(book7.have_task))
