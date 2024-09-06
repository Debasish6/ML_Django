from django import forms
from .models import Document

class ImageForm(forms.ModelForm):
    class Meta:
        model = Document
        fields='__all__'