from django.db import models

# Create your models here.
class Document(models.Model):
    image = models.ImageField(upload_to='OCR_Image_App/static/img/')
    processed_image = models.ImageField(upload_to='OCR_Image_App/static/processed_images/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)