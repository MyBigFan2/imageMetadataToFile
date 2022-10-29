from exif import Image
from fractions import Fraction
import os
from datetime import datetime as dt

## User Info ##
location = input("Shooting Location: ")
fileType = input("File extension: ")
folder = input("Folder path: ")
bitDepth = input("Color Depth: ")
# location = "GT"
# fileType = ".ARW"

## generate blank file, overwrites existing if exist ##
open((folder+"/output.txt"), 'w')
print("Generating output.txt")

## Iterate files from folder ##
for fileName in os.listdir(folder):
    if fileName.endswith(".JPG"):
        with open((folder+"\\"+fileName), 'rb') as importedImg:
            myImage = Image(importedImg)
        print("Processing", str(fileName)+"...")

## Create new .txt for output ##
        with open((folder+"/output.txt"), 'a') as outputTxt:
            print("""{Name}
Location        : {Location}
Date            : {Date}

Camera          : {Camera_maker} {Camera_model}
Lens            : {Lens_model}

Shutter Speed   : {Exposure_time}s
Aperture        : f/{F_stop}
ISO speed       : ISO {ISO_speed}
Focal Length    : {Focal_length}mm

*Original File Info*
Resolution      : {X}*{Y} ({MP}MP)
Aspect Ratio    : {Aspect_ratio}
File Format     : RAW ({Item_type})
Colour Depth    : {Bit_depth} bit\n"""
    .format(Name = fileName.split(".", 1)[0], 
            Location = location, 
            Date = dt.strftime(dt.strptime(str(myImage.datetime_original), "%Y:%m:%d %H:%M:%S"), "%d %B %Y"), 
            Camera_maker = myImage.make, 
            Camera_model = myImage.model, 
            Lens_maker = myImage.lens_specification, 
            Lens_model = myImage.lens_model,
            Exposure_time = Fraction(str(myImage.exposure_time)).limit_denominator(),
            F_stop = myImage.f_number,
            ISO_speed = myImage.photographic_sensitivity,
            Focal_length = myImage.focal_length,
            X = myImage.pixel_x_dimension,
            Y = myImage.pixel_y_dimension,
            MP = myImage.pixel_x_dimension*myImage.pixel_y_dimension/1000000,
            Aspect_ratio = str((myImage.pixel_x_dimension/myImage.pixel_y_dimension).as_integer_ratio()[0]) + ":" + str((myImage.pixel_x_dimension/myImage.pixel_y_dimension).as_integer_ratio()[1]),
            Item_type = fileType,
            Bit_depth = bitDepth),
            file = outputTxt)
        print(str(fileName), "OK")
print("Complete, output.txt at", str(folder)+"\output.txt")
input("Press [ENTER] to exit")

