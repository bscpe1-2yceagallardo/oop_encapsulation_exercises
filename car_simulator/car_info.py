class Car:
    def __init__(self, year_model: int, make: str):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__fuel = 100.0

    # GETTERS
    def get_year_model(self) -> int:
        return self.__year_model

    def get_make(self) -> str:
        return self.__make

    def get_speed(self) -> int:
        return self.__speed

    def get_fuel(self) -> float:
        return round(self.__fuel, 1)