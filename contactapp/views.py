from django.shortcuts import render
from rest_framework import viewsets
from .serializers import contactSerializers
from .models import contact

# Create your views here.
class contactView(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = contactSerializers

