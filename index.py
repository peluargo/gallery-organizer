from os import listdir, mkdir, rename
from os.path import isfile, isdir, join, splitext
from PIL import Image
from datetime import datetime
import shutil

fromDirPath = './from'
toDirPath = './to'
unknownDateDirName = 'unknown-date'
fromDatetimeFormat = '%Y:%m:%d %H:%M:%S'
toDatetimeFormat = '%Y%m%d_%H%M%S%f'
targetDirNameFormat = '%Y-%m'
totalFiles = 0
migratedFiles = 0

files = listdir(fromDirPath)

def getFileExtension(file):
    return splitext(file)[-1]

def getDatetimeFromFile(fileSourcePath):
    image = Image.open(fileSourcePath)
    return image.getexif().get(306)

def targetDirExists(targetDir):
    return isdir(targetDir)

def getTargetDirPath(fileSourcePath):
    datetimeString = getDatetimeFromFile(fileSourcePath)

    if datetimeString is not None:
        imageCreationDatetime = datetime.strptime(datetimeString, fromDatetimeFormat)
        targetDirName = datetime.strftime(imageCreationDatetime, targetDirNameFormat)
    else:
        targetDirName = unknownDateDirName

    return toDirPath + "/" + targetDirName

def getNewFileName(fileSourcePath):
    datetimeString = getDatetimeFromFile(fileSourcePath)
    if datetimeString is not None:
        imageCreationDatetime = datetime.strptime(datetimeString, fromDatetimeFormat)
        newFileName = datetime.strftime(imageCreationDatetime, toDatetimeFormat)
    else:
        newFileName = datetime.now().strftime(toDatetimeFormat)

    return newFileName

for file in files:
    if isfile(join(fromDirPath, file)):
        fileSourcePath = fromDirPath + "/" + file

        targetDirPath = getTargetDirPath(fileSourcePath)

        if not targetDirExists(targetDirPath):
            mkdir(targetDirPath)

        fileDestinationPath = targetDirPath + "/" + getNewFileName(fileSourcePath) + getFileExtension(file)

        # moves the file
        # rename(fileSourcePath, fileDestinationPath)

        # copies the file, preserving the original
        shutil.copy(fileSourcePath, fileDestinationPath)


