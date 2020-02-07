from django.shortcuts import render

# Create your views here.
from .models import Vehicle
from rest_framework import viewsets
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    

