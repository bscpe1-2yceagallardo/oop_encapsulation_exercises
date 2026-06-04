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

    # MUTATORS
    def accelerates(self):
        self.__speed =+ 5
        self.__fuel =  max(0.0, self.__fuel - 1.5)

    def brake(self):
        self.__speed = max(0,self.__speed - 5 )
        self.__fuel =  max(0.0, self.__fuel - 0.2)

    def get_gear(self) -> str:
        if self.__speed == 0:
            return "P"
        elif self.__speed <= 10:
            return "1st"
        elif self.__speed <= 20:
            return "2nd"
        else:
            return "3rd"

    def get_efficiency(self) -> str:
        if self.__speed == 0:
            return "0.0 MPG (Idling)"
        elif self.__speed > 20:
            return "18.5 MPG (Heavy Load)"
        else:
            return "32.0 MPG (Eco Cruising)"

    def __str__(self) -> str:
        return f"{self.__year_model} {self.__make}"