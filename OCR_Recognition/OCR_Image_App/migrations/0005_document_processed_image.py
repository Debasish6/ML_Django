# Generated by Django 5.1.1 on 2024-09-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCR_Image_App', '0004_document_text_alter_document_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='processed_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/processed_images/'),
        ),
    ]
