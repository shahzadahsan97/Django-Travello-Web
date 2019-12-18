from django.db import models

class Destination(models.Model):
    #id: int
    price : models.IntegerField
    desc : models.TextField
    name : models.CharField(max_length=200)
    img : models.ImageField(upload_to='pics')
    offer : models.BooleanField(default = False)


# Create your models here.
