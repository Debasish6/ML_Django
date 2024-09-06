from django.shortcuts import render
from .forms import ImageForm

# Create your views here.
def ocr_image_upload(request):
    form= ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            
    else:
        form = ImageForm()
        
    return render(request,'index.html',{'forms':form})