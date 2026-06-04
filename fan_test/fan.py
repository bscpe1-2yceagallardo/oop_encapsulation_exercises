class Fan:
    SPEED_SLOW = 1
    SPEED_MEDIUM = 2
    SPEED_FAST = 3
    SPEED_VERY_FAST = 4

def __init__(self, rotation_speed=SPEED_SLOW, blade_radius=5, chassis_color="blue", is_powered_on=False,
             target_temperature=24, is_oscillating=False, active_timer_minutes=0):