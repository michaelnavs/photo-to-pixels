"""
Author: Michael Navarro

This program will take a 50x50 image and create 25 10x10 patches.
It will then create a 25x300 list of rgb values and save to an excel sheet
"""
from typing import List
from PIL import Image
import pandas as pd


def create_pixel_list(img: Image, width: int, height: int) -> List:
    # get rgb values for each pixel in the image
    pixels = []
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


def save_25_by_300_rgb_to_excel(ten_by_ten_patch: List, image_name: str) -> None:
    # saves 25x300 dataset to an excel sheet
    ten_by_ten_df = pd.DataFrame(ten_by_ten_patch)
    writer = pd.ExcelWriter("test.xlsx", engine="xlsxwriter")
    ten_by_ten_df.to_excel(writer, sheet_name=image_name, index=False)
    writer.save()


def main() -> None:
    pass
    # create PIL.Image object and store width and height
    # img = Image.open("./img/20131001_1100.jpg")
    # width, height = img.size

    # create list of images from images directory
    # for each image:
    # create_pixel_list()
    # create_25_by_300_rgb_values()
    # save_25_by_300_rgb_to_excel()


if __name__ == "__main__":
    main()
