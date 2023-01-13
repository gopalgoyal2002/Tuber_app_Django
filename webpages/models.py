from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    number=models.CharField(max_length=10)
    create_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name

class Slider(models.Model):
    headline = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='static/media/slider/%Y/')
    create_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.headline

class Car(models.Model):
    name=models.CharField(max_length=256)
    max_speed=models.CharField(max_length=256)

