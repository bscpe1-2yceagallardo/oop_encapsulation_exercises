from pet_record import Pet

def main():
    print("----------- PET INFORMATION -----------")
    name = input("Pet Name: ")
    animal_type = input("Animal Type (ex: Dog, Cat): ")
    breed = input("Breed: ")
    age = input("Age: ")
    gender = input("Gender: ")
    color = input("Color: ")
    vaccinated = input("Are vaccinations complete? (yes/no): ")

    # OBJECTS
    my_pet = Pet()
    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)
    my_pet.set_breed(breed)
    my_pet.set_color(color)
    my_pet.set_gender(gender)
    my_pet.set_vaccinated(vaccinated)

    # USING GETTERS FETCHING AND DISPLAY DATA
    print("\n" + "=" * 40)
    print("               PET DETAILS               ")
    print("" + "=" * 40)
    print("Name:     ", my_pet.get_name())
    print("Animal Type:     ", my_pet.get_animal_type())
    print("Age:     ", my_pet.get_age())
    print("Gender:     ", my_pet.get_gender())
    print("Color:     ", my_pet.get_color())
    print("Vaccines:     ", my_pet.get_vaccinated())
    print("" + "=" * 40)

if __name__ == "__main__":
    main()