# Separates night and day images into separate folders
# later scalable by accepting dir names and string instead of "_Night"

# side note: almost all files with the string "_Night" has a matching day file
# but not all day files have a matching night file

import os
import shutil

# Set the directory to search in
rootDir = 'Images'
nightDir = 'Separated/Night'
dayDir = 'Separated/Day'
keyword = '_Night'

# list that holds the names of the files without the keyword
dayList = []

def createNightDir():
    print("Starting...")
    if not os.path.isdir(nightDir):
        os.makedirs(nightDir)
    
    for rootdir, _, files in os.walk(rootDir):
        existingFileCounter = 0
        for file in files:
            if keyword in file:
                root_filename = os.path.basename(os.path.join(rootdir, file))
                dest_filename = os.path.basename(os.path.join(nightDir, file))

                # adding the filename to the dayList after removing the keyword
                day_filename = root_filename.replace(keyword, "")
                dayList.append(day_filename)
                # print(day_filename)

                # checking if the filename exists in the destination folder
                if root_filename == dest_filename:
                    existingFileCounter += 1
                else:
                    shutil.copy(os.path.join(rootdir, file), nightDir)
        # print the number of files that already existed if any
        if existingFileCounter > 0:
            print(str(existingFileCounter) + " files with the same name have been overwritten." )

def createDayDir():
    if not os.path.isdir(dayDir):
        os.makedirs(dayDir)
    
    for name in dayList:
        fileName = os.path.join(rootDir, name)
        # if fileName exists in rootDir
        if os.path.exists(fileName):
            shutil.copy(fileName, dayDir)


def main():
    createNightDir()
    createDayDir()
    
main()

            

