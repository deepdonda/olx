from django.db import models

# Create your models here.
class image(models.Model):
    cid=models.IntegerField(max_length=10)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    mobile=models.CharField(max_length=11)
    prize=models.IntegerField(max_length=10)
    hotel_Main_Img=models.ImageField(upload_to='images/')
class cart(models.Model):
    cid=models.IntegerField(max_length=10,blank=False )