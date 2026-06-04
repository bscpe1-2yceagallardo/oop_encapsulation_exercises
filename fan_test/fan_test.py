from fan import Fan

def main():
    fan_one = Fan(Fan.SPEED_VERY_FAST,10, "yellow", True)
    fan_one.set_target_temperature(18)
    fan_one.set_is_oscillating(True)
    fan_one.set_active_timer_minutes(60)
    fan_one.device_summary("FAN 1")

    fan_two = Fan(Fan.SPEED_MEDIUM,5, "blue", False)
    fan_one.device_summary("FAN 2")

if __name__ == "__main__":
    main()