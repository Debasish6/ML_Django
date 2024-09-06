from django.shortcuts import render
from .forms import ImageForm
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image

# Create your views here.
def ocr_image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            image = Image.open(img.image.path)
            decodec_text = pytesseract.image_to_string(image)
            img.text = decodec_text
            img.save()
            return render(request, 'index.html', {'img': img})
    else:
        form = ImageForm()
        
    return render(request, 'index.html', {'form': form})

    