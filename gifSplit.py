from PIL import Image
import os
import getopt
import sys

outputfolder = ''
inputfile = ''
try:
    options, arguments = getopt.getopt(sys.argv[1:], "i:o:", ["help"])
except getopt.GetoptError:
    print("Usage: gifSplit.py -i <inputfile> -o <outputfolder>")
    sys.exit(2)
for option, argument in options:
    if option == '--help':
        print("Usage: gifSplit.py -i <inputfile> -o <outputfolder>")
        sys.exit(2)
    elif option == "-o":
        outputfolder = argument + "/"
    elif option == "-i":
        inputfile = argument
if not os.path.exists(outputfolder):
    os.makedirs(outputfolder)
image = Image.open(inputfile)
done = False
currentFrame = image.seek(image.tell())
while not done:
    newFrame = Image.new('RGBA', image.size)
    newFrame.paste(image)
    newImageDest = os.path.join(outputfolder, "(" + str(image.tell() + 1) + ").png")
    newFrame.save(newImageDest)
    try:
        image.seek(image.tell() + 1)
    except EOFError:  # Called if we run out of frames
        done = True
