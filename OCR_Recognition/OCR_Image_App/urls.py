from django.urls import path
from . import views

urlpatterns = [
    path('', views.ocr_image_upload, name='ocr_image_upload'),
    # path('ocr_text/<int:pk>',views.ocr_text, name='ocr_text'),
]