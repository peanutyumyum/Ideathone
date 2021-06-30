from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    

class Garden(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name