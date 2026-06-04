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

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def set_breed(self, breed):
        self.__breed = breed

    def set_color(self, color):
        self.__color = color

    def set_gender(self, gender):
        self.__gender = gender

    def set_vaccinatedr(self, status):
        if status.lower() in ['yes', 'y', 'complete']:
            self.__vaccinated = "Complete"
        else:
            self.__vaccinated = "Not Complete"

    # GETTERS
    def set_name(self):
        return self.__name

    def set_animal_type(self):
        return self.__animal_type

    def set_age(self):
        return self.__age

    def set_breed(self):
        return self.__breed