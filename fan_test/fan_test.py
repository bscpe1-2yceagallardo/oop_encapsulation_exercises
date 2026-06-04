from fan import Fan

def main():
    fan_one = Fan(Fan.SPEED_VERY_FAST,10, "yellow", True)
    fan_one.set_target_temperature(18)
    fan_one.set_is_oscillating(True)
    fan_one.set_active_timer_minutes(60)
    fan_one.device_summary("FAN 1")