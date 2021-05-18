from typing import Tuple

import math


def center_x_y(x: int, y: int) -> Tuple:
    origin_x = 357
    origin_y = 255

    new_x = x - origin_x
    new_y = origin_y - y

    return new_x, new_y


def is_black(pixel: Tuple) -> bool:
    return pixel == (0, 0, 0)


def is_white(pixel: Tuple) -> bool:
    return pixel == (255, 255, 255)


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

    a = math.sqrt(center_x ** 2 + (center_y ** 2) / (1 - e ** 2))

    altitude = -0.3253 * a + 92.415

    return altitude


def get_azimuth(psi):
    azimuth = 0.9625 * psi + 1.7688

    return azimuth


def get_central_angle(altitude_point, azimuth_point, altitude_sun, azimuth_sun):
    azimuth_1_2 = azimuth_sun - azimuth_point

    tan_central_angle = (
        math.sqrt(
            (
                math.cos(altitude_point) * math.sin(altitude_sun)
                - math.sin(altitude_point)
                * math.cos(altitude_sun)
                * math.cos(azimuth_1_2)
            )
            ** 2
            + (math.cos(altitude_sun) * math.sin(azimuth_1_2)) ** 2
        )
    ) / (
        math.sin(altitude_point) * math.sin(altitude_sun)
        + math.cos(altitude_point) * math.cos(altitude_sun) * math.cos(azimuth_1_2)
    )

    # tangent to radians by atan()
    central_angle = math.atan(tan_central_angle)

    if central_angle < 0:
        central_angle += math.radians(180)

    return math.degrees(central_angle)


def calculate_rho():
    # ppt slide 14
    pass


def calculate_theta_psi(x, y):
    theta = psi = 0

    if x > 0 and y > 0:
        theta = math.atan(y / x)
        psi = theta + 3 * math.pi / 2
    elif x > 0 and y < 0:
        theta = 2 * math.pi + math.atan(y / x)
        psi = theta - math.pi / 2
    elif (x < 0 and y > 0) or (x < 0 and y < 0):
        theta = math.pi + math.atan(y / x)
        psi = theta - math.pi / 2

    return theta, math.degrees(psi)  # theta is in radians, psi is in degrees
