"""
Author: Michael Navarro

This program will take a 50x50 image and create 25 10x10 patches.
It will then create a 25x300 list of rgb values and save to an excel sheet
"""

from PIL import Image

img = Image.open("./img/20131001_1100.jpg")
width, height = img.size

total_pixels = []
for y in range(height):
    for x in range(width):
        total_pixels.append(img.getpixel((x, y)))

# print(len(total_pixels)) -> 2500 total pixels

for pixel in total_pixels:
    print(pixel, end=" ")

ten_by_ten_collection = []
for y in range(0, height, 10):
    for x in range(0, width, 10):
        ten_by_ten = []
        for k in range(100):
            ten_by_ten.append(total_pixels[x + k + y * width])
        ten_by_ten_collection.append(ten_by_ten)

for ten_by_ten in ten_by_ten_collection:
    print(ten_by_ten)
