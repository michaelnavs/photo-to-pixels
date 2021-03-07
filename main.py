"""
Author: Michael Navarro

This program will take a 50x50 image and create 25 10x10 patches.
It will then create a 25x300 list of rgb values and save to an excel sheet
"""

from PIL import Image
import pandas as pd

# create PIL.Image object and store width and height
img = Image.open("./img/20131001_1100.jpg")
width, height = img.size

# get rgb values for each pixel in the image
pixels = []
for y in range(height):
    for x in range(width):
        pixels.append(img.getpixel((x, y)))

# print(len(pixels)) -> 2500 total pixels

# print the each pixel value in pixels array
for pixel in pixels:
    print(pixel, end=" ")

print(end="\n\n")

# create 10x10 patches
ten_by_ten_list = []
for y in range(0, height, 10):
    for x in range(0, width, 10):
        ten_by_ten = []
        for i in range(10):
            for j in range(10):
                for k in range(3):
                    ten_by_ten.append(pixels[x + j + (y + i) * width][k])
        ten_by_ten_list.append(ten_by_ten)

# print each 10x10 patch and its respective length
for ten_by_ten in ten_by_ten_list:
    print(ten_by_ten, len(ten_by_ten), sep=" ", end="\n\n")

ten_by_ten_df = pd.DataFrame(ten_by_ten_list)
writer = pd.ExcelWriter("test.xlsx", engine="xlsxwriter")
ten_by_ten_df.to_excel(writer, sheet_name="test", index=False)
writer.save()
