import glob, sys
from generateClearSkyImageWithCentralAngle import generateClearSkyImage


def main() -> None:
    BLACK_PIXEL = (0, 0, 0)
    image_filenames = glob.glob("./images/*.jpg")
    image_filenames.sort()  # alaphabetically sort the list of file names

    tadjs = [0.08611111, 0.05472222, 0.03527778]
    declinations = [-0.3671597, -0.3455368, -0.1360118]

    for i, image_filename in enumerate(image_filenames):
        print(f"{image_filename}...")  # display file name to see progress
        generateClearSkyImage(image_filename, tadjs[i], declinations[i])


if __name__ == "__main__":
    sys.exit(main())
