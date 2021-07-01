from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    price = models.IntegerField()
    water_period = models.TextField()
    proper_place = models.TextField()
    temperature = models.TextField()
    caution = models.TextField()
    image = image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    

class Garden(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    place_size = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name