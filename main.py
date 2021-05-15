from PIL import Image
import pandas as pd
import glob
from utils import (
    center_x_y,
    is_black,
    is_white,
    is_blue_sky,
    get_altitude,
    get_azimuth,
    get_central_angle,
    selection_criteria,
)


def main() -> None:
    image_filenames = glob.glob("./images/*.jpg")
    # image_filenames.sort() # alaphabetically sort the list of file names

    for image_filename in image_filenames:
        print(f"{image_filename}...")  # display file name to see progress
        image = Image.open(image_filename)  # create instance of Pillow.Image
        width, height = image.size
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))  # tuple of RGB values -> (R, G, B)
                # skip pixels that are pure black, pure white, and not blue sky pixels
                if is_black(pixel) or is_white(pixel) or not (is_blue_sky):
                    continue
                center_x, center_y = center_x_y(x, y)
                altitude = get_altitude(center_x, center_y)
                azimuth = get_azimuth(center_x, center_y)
                central_angle = get_central_angle(altitude, azimuth)
                # if alititude and central angle do not meet the criteria, set RGB value to black
                if not (selection_criteria(altitude, central_angle)):
                    image.putpixel((x, y), (0, 0, 0))
        image.show()


if __name__ == "__main__":
    main()
