from PIL import Image
import os
import sys

workingDir = os.getcwd()
for filename in os.listdir(workingDir):
    if filename.endswith(".jpg") || filename.endswith("png"):
        image = Image.open(filename)
        pixels = image.load();
        #for each jpg file in directory, open it in the image variable, load pixels.
        print(image.format, image.size, image.mode)
        savedPixels = [0,0]
        for x in image.size[0]*imageSize[1]: #Hit every pixel if neccesary
            
