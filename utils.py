from typing import Tuple

from typing import Tuple


def center_x_y(x: int, y: int) -> Tuple:
    origin_x = 357
    origin_y = 255

    new_x = x - origin_x
    new_y = origin_y - y

    return new_x, new_y


def is_black():
    # slide 14
    pass


def is_white():
    # slide 14
    pass


def is_sky_region():
    pass


def is_blue_sky():
    # ppt slide 13
    pass


def selection_criteria():
    # ppt slide 13
    pass


def get_altitude(center_x, center_y):
    # e is epsilon
    e = 0.417

    a = sqrt(center_x**2 + (center_y**2)/(1-e**2))
    
    altitude = -0.3253*a + 92.415

    return altitude
    


def get_azimuth():
    # ppt slide 7
    pass


def get_central_angle():
    # ppt slide 9
    pass


def calculate_rho():
    # ppt slide 14
    pass


def calculate_theta():
    # ppt slide 7
    pass


def calculate_psi():
    # ppt slide 7
    pass
