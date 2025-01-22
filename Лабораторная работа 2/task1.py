BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book

class Book:
    def __init__(self, id, name, pages):
        if not isinstance(id, (int, float)):
            raise TypeError('id книги должен иметь тип int или float')
        if id <= 0:
            raise ValueError('id книги должен быть положительным числом')
        self.id = id

        if not isinstance(name, str):
            raise TypeError('Имя книги должно быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('количество страниц книги должно быть типа int')
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id =book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__