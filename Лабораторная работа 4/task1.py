if __name__ == "__main__":
    # Write your solution here

    class Drink():

        def __init__(self, price, temp):
            """
            :param price: цена напиктка
            :param temp: температура напитка
            """
            if not isinstance(price, (int, float)):
                raise TypeError("Цена напитка должна быть числом.")
            if price < 0:
                raise ValueError('Цена должна быть больше нуля')
            self.price = price

            if not isinstance(temp, (int, float)):
                raise TypeError("Температура напитка должна быть числом.")
            if temp < 0:
                raise ValueError('Температура должна быть больше нуля')
            self.temp = temp

        def __str__(self):
            """
            Строчное представление класса
            :return: str
            """
            return f"Напиток за {self.price}. Температура - {self.temp}"

        def __repr__(self):
            return f"{self.__class__.__name__}(price={self.price!r}, temp={self.temp!r})"

        def temp_determine(self):
            """
            Определение по температуре состояние напитка
            :return: str
            """
            if self.temp <= 30:
                return 'Напиток холодный'
            if (self.temp >= 30 and self.temp < 60):
                return 'Напиток теплый'
            if self.temp >= 60:
                return 'Напиток горячий'

        def contraindications(self):
            """
            Выписывает противопоказания
            :return: str
            """
            return 'Напиток можно употреблять всем'

    class Milk(Drink):

        def __init__(self, price, temp):
            super().__init__(price, temp)
            """
            :param price: цена напитка
            :param temp: температура напитка
            """

        def  contraindications(self):
            """
            Перегрузка вызвана по причине, что у данного напитка есть противопоказания
            Выписывает противопоказания
            :return: str
            """
            return super().contraindications() + ', кроме людей с непереносимостью лактозы'

        def temp_determine(self):
            """
            Определение по температуре состояние напитка
            :return: str
            """
            return super().temp_determine()


        def __str__(self):
            return super().__str__()

        def __repr__(self):
            return super().__repr__()



else:
    pass

drink = Milk(5, 50)
print(drink.temp_determine(),'.', drink.contraindications())