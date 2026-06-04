class Fan:
    SPEED_SLOW = 1
    SPEED_MEDIUM = 2
    SPEED_FAST = 3
    SPEED_VERY_FAST = 4

    def __init__(self, rotation_speed=SPEED_SLOW, blade_radius=5, chassis_color="blue", is_powered_on=False,
             target_temperature=24, is_oscillating=False, active_timer_minutes=0):
             self.__rotation_speed = rotation_speed
             self.__blade_radius = blade_radius
             self.__chassis_colors = chassis_color
             self.__is_powered_on = is_powered_on
             self.__target_temperature = target_temperature
             self.__is_oscillating = is_oscillating
             self.__active_timer_minutes = active_timer_minutes

    # GETTERS
    def get_rotation_speed(self):
        return self.__rotation_speed

    def get_blade_radius(self):
        return self.__blade_radius

    def get_chassis_colors(self):
        return self.__chassis_colors

    def get_is_powered_on(self):
        return self.__is_powered_on

    def get_target_temperature(self):
        return self.__target_temperature