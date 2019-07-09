from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
    first_name= models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)