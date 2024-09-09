from django.shortcuts import render
from .forms import ImageForm
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
import cv2
from django.core.files.base import ContentFile

# Create your views here.
def ocr_image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            image = cv2.imread(img.image.path)
            
            #Preprocessing
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, buffer = cv2.imencode('.jpg', gray_image)
            processed_image = ContentFile(buffer.tobytes())
            
            img.processed_image.save(f'processed_{img.image.name}', processed_image)
            img.save()
            
            #Extracting Text from Processed image
            image = Image.open(img.processed_image.path)
            decodec_text = pytesseract.image_to_string(image)
            img.text = decodec_text
            img.save()
            return render(request, 'result.html', {'img': img})
    else:
        form = ImageForm()
        
    return render(request, 'index.html', {'form': form})

    

    