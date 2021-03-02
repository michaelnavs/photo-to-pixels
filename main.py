"""
Author: Michael Navarro

This program will take a 50x50 image and create 25 10x10 patches.
It will then create a 25x300 list of rgb values and save to an excel sheet
"""

from PIL import Image
import numpy as np

img = Image.open("./img/20131001_1100.jpg")
total_pixels = []

for x in range(img.size[0]):
    for y in range(img.size[1]):
        total_pixels.append(img.getpixel((x, y)))

for pixel in total_pixels:
    print(pixel)
