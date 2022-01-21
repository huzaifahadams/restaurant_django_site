from django.db import models

# Create your models here.
class Menu(models.Model):
    heading= models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    #image= models.ImageField()
    cost = models.CharField(max_length=50)
    details = models.CharField(max_length=500)


class Blog(models.Model):
    head = models.CharField(max_length=200)
    #image= models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    content = models.CharField(max_length=500)
    









    