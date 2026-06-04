class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
        self.__breed = ""
        self.__color = ""
        self.__gender = ""
        self.__vaccinated = ""

    # SETTERS
    def set_name(self, name):
        self.__name = name

    def set_name(self, animal_type):
        self.__animal_type = animal_type