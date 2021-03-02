"""
Author: Michael Navarro

This program will take a 50x50 image and create 25 10x10 patches.
It will then create a 25x300 list of rgb values and save to an excel sheet
"""

from PIL import Image

img = Image.open("./img/20131001_1100.jpg")
width, height = img.size
total_pixels = []

for i in range(height):
    for j in range(width):
        total_pixels.append(img.getpixel((j, i)))

# print(len(total_pixels)) -> 2500 total pixels

# for pixel in total_pixels:
#    print(pixel, end=" ")
