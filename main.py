from PIL import Image
from pytesseract import pytesseract
import os
f = open("Output File.txt", "a+")
# clear previous content of file
f.seek(0)
f.truncate()
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR/tesseract.exe'
#Define path to image
path_to_images = r'images/'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
i = 0
for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file_name in the folder
    for file_name in file_names:
        # image number
        i+=1
        print("Image",i,"\n")
        #Open image with PIL
        img = Image.open(path_to_images + file_name)
        #Extract text from image
        text = pytesseract.image_to_string(img)
        print(text)
        # Writing into txt file
        image_num = "Image " + str(i) + "\n"
        f.write(image_num)
        f.write(text)
        f.write("------------------------------------------------------------\n")

f.close()