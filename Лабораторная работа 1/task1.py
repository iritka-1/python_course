# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class mobile_phone:
    def __init__(self, safety_glass: bool):
        """
                Создание и подготовка к работе объекта "Телефон"

                :param charge: заряд батареи телефона
                :param safety_glass: наличие защитного стекла

                Примеры:
                >>> phone = mobile_phone(True)  # инициализация экземпляра класса
                """
        self.charge=100
        if not isinstance(safety_glass,bool):
            raise TypeError('type must be bool')

        self.safety_glass=safety_glass

    def ChargingPhone(self,time):
        """
                Функция которая позволяет зарядить телефон
                :param time: время телефона на зарядке
                :raise ValueError: Если время отрицательное, то вызываем ошибку

                Примеры:
                >>> phone = mobile_phone(True)
                >>> phone.ChargingPhone(10)
                """
        if not isinstance(time,int):
            raise TypeError('type must be int')
        if time<0:
            raise ValueError('time must be positive')
        self.charge+= time
        if self.charge>100:
            self.charge=100
    def PlayVideoGame(self):
        """
        Функция тратящая заряд устройства
        :raise ValueError: Если заряда телефона нехватает, то возвращается ошибка
        Примеры:
        >>> phone = mobile_phone(True)
        >>> phone.PlayVideoGame()
        """
        if self.charge<10:
            raise ValueError('charge must be >=10')

    def RemoveSafetyGlass(self):
        """
        Функция позволяющая снять защитное стекло
        :raise ValueError: если стекла нет, то возвращается ошибка
        >>> phone = mobile_phone(True)
        >>> phone.RemoveSafetyGlass()
        """
        if self.safety_glass==False:
            raise ValueError('safety_glass must be true')
        self.safety_glass=False

class Student:
    def __init__(self,age :int,):
        """
                Создание и подготовка к работе объекта "Студент"

                :param age: возраст студента
                :param scholarship: наличие стипендии

                Примеры:
                >>> student = Student(18)  # инициализация экземпляра класса
        """
        if not isinstance(age,int):
            raise ValueError('age must be int')
        self.scholarship=True
        self.age=age
    def session(self):
        """
                Функция предназначенная только для того чтобы лишать студента стипендии
                :raise ValueError: если стипендии нет, то метод не применим

                >>> student=Student(18)
                >>> student.session()
                """


        if self.scholarship==False:
            raise ValueError('must be True')
        self.scholarship=False
    def birthday(self):
        """
        Функция увеличивающая возраст студента на 1 год
        Примеры:
        >>> student = Student(18)
        >>> student.birthday()
        """
        self.age+=1

class Bed:
    def __init__(self,width: int, length:int):
        """
            Создание и подготовка к работе объекта "Кровать"

                :param width: ширина кровати
                :param length: длинна кровати

                Примеры:
                >>> bed = Bed(3,2)  # инициализация экземпляра класса
        """
        if not isinstance(width,int):
            raise TypeError('must be int')
        if width<=0:
            raise ValueError('must be >0')
        if not isinstance(length,int):
            raise TypeError('must be int')
        if length<=0:
            raise ValueError('must be >0')
        self.width=width
        self.length=length
        self.made_bed=True
    def MakeTheBed(self):
        """
            Функция которая заправляет кровать
            :raise ValueError: Если кровать уже заправлена то вызывает ошибку
            Пример:
            >>> bed = Bed(3,2)
            >>> bed.UnMakeTheBed()
            >>> bed.MakeTheBed()

        """
        if self.made_bed==True:
            raise ValueError('must be False')
        self.made_bed=True
    def UnMakeTheBed(self):
        """
                    Функция которая устраивает на кровати беспорядок
                    :raise ValueError: Если кровать уже в ужасном состоянии то вызывает ошибку
                    Пример:
                    >>> bed = Bed(3,2)
                    >>> bed.UnMakeTheBed()

                """
        if self.made_bed==False:
            raise ValueError('must be True')
        self.made_bed=False





if __name__ == "__main__":
    student=Student(18)
    pass
