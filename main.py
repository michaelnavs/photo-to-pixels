from PIL import Image
import glob
from utils import (
    calculate_theta_psi,
    center_x_y,
    is_black,
    is_white,
    is_blue_sky,
    is_sky_region,
    get_altitude,
    get_azimuth,
    get_central_angle,
    selection_criteria,
    get_sun_altitude_azimuth,
)


def main() -> None:
    BLACK_PIXEL = (0, 0, 0)
    image_filenames = glob.glob("./images/*.jpg")
    image_filenames.sort()  # alaphabetically sort the list of file names

    tadjs = [0.08611111, 0.05472222, 0.03527778]
    declinations = [-0.3671597, -0.3455368, -0.1360118]

    for i, image_filename in enumerate(image_filenames):
        print(f"{image_filename}...")  # display file name to see progress
        image = Image.open(image_filename)  # create instance of Pillow.Image
        width, height = image.size
        sun_altitude, sun_azimuth = get_sun_altitude_azimuth(
            image_filename, tadjs[i], declinations[i]
        )
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))  # tuple of RGB values -> (R, G, B)
                # get new x and y values based on center of sky region
                center_x, center_y = center_x_y(x, y)
                theta, psi = calculate_theta_psi(center_x, center_y)  # get theta, psi
                # turn pixels to black and skip them that are pure black, pure white, and not within sky region
                if (
                    is_black(pixel)
                    or is_white(pixel)
                    or not (is_sky_region(center_x, center_y, theta))
                ):
                    image.putpixel((x, y), BLACK_PIXEL)
                    continue
                altitude = get_altitude(center_x, center_y)
                azimuth = get_azimuth(psi)
                central_angle = get_central_angle(
                    altitude, azimuth, sun_altitude, sun_azimuth
                )
                # if alititude and central angle do not meet the criteria or pixel is not a blue sky pixel, set RGB value to black
                if not (selection_criteria(altitude, central_angle)) or not (
                    is_blue_sky(pixel)
                ):
                    image.putpixel((x, y), BLACK_PIXEL)
        new_filename = image_filename[:-4] + "_output.jpg"
        image.save(new_filename)
        image.show()


if __name__ == "__main__":
    main()
