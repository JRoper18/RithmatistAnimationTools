from PIL import Image
import os

workingDir = os.getcwd()
fileCount = 0
for filename in os.listdir(workingDir):
    fileCount += 1
    if filename.endswith(".jpg") or filename.endswith("png") or filename.endswith("gif"):
        image = Image.open(filename)
        # for each jpg or png file in directory, open it in the image variable, load pixels.
        print(image.format, image.size, image.mode)
        image = image.convert('RGBA')
        colorToCheck = image.getpixel((0, 0))
        if not colorToCheck[3] == 0:
            pixelStack = [(0, 0)]
            while(len(pixelStack) > 0):
                currentPixel = pixelStack.pop()
                if image.getpixel(currentPixel) == colorToCheck:
                    image.putpixel(currentPixel, (0, 0, 0, 0))
                    if currentPixel[0] < image.size[0] - 1:
                        # Check if out of bounds
                        pixelStack.append((currentPixel[0] + 1, currentPixel[1]))
                    if currentPixel[1] < image.size[1] - 1:
                        pixelStack.append((currentPixel[0], currentPixel[1] + 1))
                    if currentPixel[0] > 0:
                        pixelStack.append((currentPixel[0] - 1, currentPixel[1]))
                    if currentPixel[1] > 0:
                        pixelStack.append((currentPixel[0], currentPixel[1] - 1))
            newImageDest = "(" + str(fileCount) + ").png"
            image.save(newImageDest)
