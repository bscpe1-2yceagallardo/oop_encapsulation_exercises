class Car:
    def __init__(self, year_model: int, make: str):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__fuel = 100.0