from django.db import models

# Create your models here.
class Document(models.Model):
    image = models.ImageField(upload_to='img/')
    # text = models.TextField(blank=True, null=True)