from pyexpat import model
from django.db import models


# Create your models here.

class list4(models.Model):
    img = models.CharField(max_length=2550)
    name = models.CharField(max_length=255)
    price= models.IntegerField()
    content = models.CharField(max_length=700)
    
  