class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self.name
    def author(self):
        return self.author


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()}. Страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, (int, float)):
            raise ValueError("Продолжительность должна быть числом.")
        if duration < 0:
            raise ValueError("Продолжительность не может быть отрицательной.")
        self.duration = duration

    def __str__(self):
        return  f"{super().__str__()}. Длительность {self.duration} минут"
