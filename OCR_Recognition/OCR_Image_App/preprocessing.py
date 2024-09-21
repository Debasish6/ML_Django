import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
import numpy as np
import cv2
from django.core.files.base import ContentFile

#Preprocessing using Open CV
def image_processing(img):
    image = cv2.imread(img.image.path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Converted to grayscale image.")
    
    thresh=cv2.threshold(gray_image,120,230,cv2.THRESH_BINARY)[1]
    print("Threshold Applied sucessfully.")
    
    _, buffer = cv2.imencode('.jpg', thresh)
    print("Encoded thresh image to JPG format.")
    
    processed_image = ContentFile(buffer.tobytes())
    return processed_image

#Extracting Text from Processed image
def extract_text(pre_image):
    processed_image = Image.open(pre_image.processed_image.path)
    decodec_text = pytesseract.image_to_string(processed_image)
    return decodec_text

def structured_text(text):
    lines = dict()
    i=0
    w=''
    for line in text:
        w = w+line
        if line == "\n":
            lines[i]=w
            i=i+1
            w=''
    return lines