import time

from car_info import Car

def display_dashboard(car: Car, action: str):
    print("\n" + "=" * 40)
    print(f"  Status  : {action.upper()}")
    print(f"  Vehicle  : {car.get_make()} ({car.get_year_model()})")
    print(f"  Status  : {car.get_speed()} MPH")
    print(f"  Status  : [{car.get_gear()}]")
    print("\n" + "=" * 40)
    print(f"  Fuel Level  : {car.get_fuel()}%")
    print(f"  Eco Rating  : {car.get_efficiency()}")
    print("\n" + "=" * 40)

def main():
    print("--- CAR SIMULATOR ---")

    while True:
        try:
            year = int(input("Enter Car Year Model (ex: 2026): "))
            if year < 1886:
                print("Cars didn't exist back then! Try again.")
                continue
            break
        except ValueError:
            print("Invalid Input. Please enter numeric year.")

    make = input("Enter Car Make/Model (ex: Tesla, Ford):").strip()
    if not make:
        make = "Generic Vehicle"

    my_car = Car(year, make)
    print(f"\nSuccessfully spawned your {my_car}!")
    time.sleep(1)

    # Acceleration phase
    print("\nPUSHING THE GAS PEDAL...")
    for i in range(5):
        time.sleep(0.5)
        my_car.accelerates()
        display_dashboard(my_car, "Accelerating")

    time.sleep(1.5)

    print("\nSLAMMING THE BRAKES...")
    for i in range(5):
        time.sleep(0.5)
        my_car.brake()
        display_dashboard(my_car, "Braking")

    print("\nSimulation complete. Vehicle safely parked.")

if __name__ == "__main__":
    main()