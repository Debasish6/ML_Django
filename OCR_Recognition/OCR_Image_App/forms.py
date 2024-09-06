from django import forms
from .models import Documents

class ImageForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields='__all__'