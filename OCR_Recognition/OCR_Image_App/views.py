from django.shortcuts import render
from .forms import ImageForm
from .preprocessing import image_processing,extract_text,structured_text

# Create your views here.
def ocr_image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            
            #Doing some preprocessing
            processed_image = image_processing(img)
            img.processed_image.save(f'processed_{img.image.name}', processed_image)
            img.save()
            
            #Storing the extracted text to decodec_text
            decodec_text= extract_text(img)
            img.text = decodec_text
            img.save()
            
            text = structured_text(decodec_text)
            
            #Printing the extracted text
            print("\nExtracted text from image :")
            for i in text.values():
                print(i ,end="")
                
            context = {'img':img}
            return render(request, 'result.html', context)
    else:
        form = ImageForm()
        
    return render(request, 'index.html', {'form': form})







    

    