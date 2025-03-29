from django.shortcuts import render
from rest_framework import viewsets
from .serializers import contactSerializers,bookSerializers,authorSerializers
from .models import contact,Book,Author

# Create your views here.
class contactView(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = contactSerializers


class bookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = bookSerializers 

class authorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = authorSerializers    