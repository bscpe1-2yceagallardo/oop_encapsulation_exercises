from car_info import Car

def display_dashboard(car: Car, action: str):
    print("\n" + "=" * 40)
    print(f"  Status  : {action.upper()}")
    print(f"  Vehicle  : {car.get_make()} ({car.get_year_model})")
    print(f"  Status  : {car.get_speed()} MPH")
    print(f"  Status  : [{car.get_gear}]")
    print("\n" + "=" * 40)
    print(f"  Fuel Level  : {car.get_fuel}%")
    print(f"  Eco Rating  : {car.get_efficiency}")
    print("\n" + "=" * 40)