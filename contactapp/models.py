from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    address = models.TextField( )

