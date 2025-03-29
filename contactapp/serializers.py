from rest_framework import serializers
from .models import contact


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

