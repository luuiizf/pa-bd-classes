from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Item
from .serializers import ClienteSerializer, ItemSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
