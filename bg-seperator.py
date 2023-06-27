# Separates night and day images into separate folders
# later scalable by accepting dir names and string instead of "_Night"

# Iterate through the images and find the ones with "_Night" in the name
# TODO: Remove the word "_Night" from the file name and add them to a list

import os
import shutil

# Set the directory to search in
rootDir = 'Images'
nightDir = 'Separated/Night'
dayDir = 'Separated/Day'
keyword = '_Night'


def main():
    print("Starting...")
    if not os.path.exists(nightDir):
        os.makedirs(nightDir)
    if not os.path.exists(dayDir):
        os.makedirs(dayDir)
    for rootdir, _, files in os.walk(rootDir):
        existingFileCounter = 0
        for file in files:
            if keyword in file:
                # copy file to new directory using shutil.copy function
                try: 
                    shutil.copy(os.path.join(rootdir, file), nightDir)
                except shutil.SameFileError:
                    existingFileCounter += 1
                    shutil.copy2(os.path.join(rootdir, file), nightDir)
        # print the number of files that already existed if any
        if existingFileCounter > 0:
            print(str(existingFileCounter) + " files with the same name have been overwritten." )



main()

            

