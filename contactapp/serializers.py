from rest_framework import serializers
from .models import contact,Author,Book


class contactSerializers(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ['name','email','phone','address']

        extra_kwargs ={
               "name":{
                   "min_length":3,
                   "error_messages":{"min_length":"name Must be three characters"},
                   
               },
               # "address":{"required" : False}  
        }


class authorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class bookSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all()
    )
    class Meta:
        model = Book
        fields = ['name','author']        
