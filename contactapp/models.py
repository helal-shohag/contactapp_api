from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    address = models.TextField( )

    def __str__(self):
       return self.name





class Author(models.Model):
    name = models.CharField(max_length=20)



    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(Author,on_delete= models.CASCADE)

    def __str__(self):
        return self.name
