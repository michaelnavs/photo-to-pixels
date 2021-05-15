"""
Author: Michael Navarro

This program will take a 50x50 image and create 25 10x10 patches.
It will then create a 25x300 list of rgb values, remove the red values,
and saves the ratios of Blue/Green to an excel sheet
"""
from typing import List
from PIL import Image
import pandas as pd
import glob


def create_pixel_list(img: Image, width: int, height: int) -> List:
    # get rgb values for each pixel in the image
    pixels = []  # each index stores tuple of rgb values
    for y in range(height):
        for x in range(width):
            pixels.append(img.getpixel((x, y)))
    return pixels


def create_25_by_300_rgb_values(pixel_array: List, width: int, height: int) -> List:
    # create 10x10 patches from image, convert to 25x300 dataset of pixel values
    ten_by_ten_list = []
    for y in range(0, height, 10):
        for x in range(0, width, 10):
            ten_by_ten = []
            for i in range(10):
                for j in range(10):
                    for k in range(3):
                        ten_by_ten.append(pixel_array[x + j + (y + i) * width][k])
            ten_by_ten_list.append(ten_by_ten)
    return ten_by_ten_list


def remove_red_values(pixel_patches: List) -> List:
    # populate indices list with multiples of 3 until 300
    indices = [iter for iter in range(300) if iter % 3 == 0]
    blue_green_patches = []
    for patch in pixel_patches:
        # sort indices from high to low, need to remove values from patch with higher index to not affect lower indexes
        for i in sorted(indices, reverse=True):
            del patch[i]
        blue_green_patches.append(patch)

    return blue_green_patches


def get_blue_green_ratios(blue_green_patches: List) -> List:
    # created patches of Blue / Green ratio values
    blue_green_ratio_patches = []
    for patch in blue_green_patches:
        blue_green_ratio_patch = []
        for i in range(0, len(patch), 2):
            blue_green_ratio = patch[i + 1] / patch[i]
            blue_green_ratio_patch.append(blue_green_ratio)
        blue_green_ratio_patches.append(blue_green_ratio_patch)
    return blue_green_ratio_patches


def add_25_by_300_rgb_to_excel(
    ten_by_ten_patch: List, writer: pd.ExcelWriter, row_position: int
) -> None:
    # adds 25x300 dataset to an excel sheet
    ten_by_ten_df = pd.DataFrame(ten_by_ten_patch)
    ten_by_ten_df.to_excel(
        writer, sheet_name="data", index=False, startrow=row_position, header=False
    )


def main() -> None:
    row_position = 0
    row_offset = 25

    image_filenames = glob.glob("./images/*.jpg")
    image_filenames.sort()  # alphabetically sort the list

    writer = pd.ExcelWriter("dataset.xlsx", engine="xlsxwriter")

    for image_filename in image_filenames:
        print(f"working on pixel dataset for {image_filename}")
        image = Image.open(image_filename)
        width, height = image.size
        pixels = create_pixel_list(image, width, height)
        pixel_patches = create_25_by_300_rgb_values(pixels, width, height)
        blue_green_pixel_patches = remove_red_values(pixel_patches)
        blue_green_ratios = get_blue_green_ratios(blue_green_pixel_patches)
        add_25_by_300_rgb_to_excel(blue_green_ratios, writer, row_position)
        row_position += row_offset
    writer.save()
    print("Done!")


if __name__ == "__main__":
    main()