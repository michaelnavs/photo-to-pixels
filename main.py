import glob, sys, pandas as pd
from generateClearSkyImageWithCentralAngle import generateClearSkyImage


def main() -> int:
    image_filenames = glob.glob("./images/*/*.jpg")
    image_filenames.sort()  # alaphabetically sort the list of file names

    df = pd.read_excel("sun_data.xlsx", sheet_name="DATA")
    dates = df["Date"].to_list()
    tadjs = df["TADJ (h)"].to_list()
    declinations = df["d (rad)"].to_list()

    for image_filename in image_filenames:
        print(f"{image_filename}...")  # display file name to see progress
        date = int(image_filename[9:17])  # get date from filename
        idx = dates.index(date)  # returns the index of the date in dates
        print(tadjs[idx], declinations[idx])
        generateClearSkyImage(image_filename, tadjs[idx], declinations[idx])

    return 0


if __name__ == "__main__":
    sys.exit(main())
