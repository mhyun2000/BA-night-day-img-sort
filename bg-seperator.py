# Separates night and day images into separate folders
# later scalable by accepting dir names and string instead of "_Night"

# Iterate through the images and find the ones with "_Night" in the name
# TODO: Remove the word "_Night" from the file name and add them to a list

import os
import shutil

# Set the directory you want to start from
rootDir = 'Images'
nightDir = 'Separated/Night'
dayDir = 'Separated/Day'
keyword = '_Night'


def main():
    print("Starting...")
    os.makedirs(nightDir)
    os.makedirs(dayDir)
    for rootdir, _, files in os.walk(rootDir):
        for file in files:
            if keyword in file:
                print("Matching file found.")
                # copy file to new directory using shutil.copy function
                shutil.copy(os.path.join(rootdir, file), nightDir)

main()

            

