from tkinter.constants import CASCADE

from django.db import models
from django.forms import CharField


class Brands(models.Model):
    name = models.CharField(max_length=150)

def __str__(self):
    self.name



class Cars(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    narxi = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='myfiles/photos/',blank=True,null=True)
    color = models.CharField(max_length=50)
    category = models.ForeignKey(Brands,on_delete=models.CASCADE)

def __str__(self):

    self.name








