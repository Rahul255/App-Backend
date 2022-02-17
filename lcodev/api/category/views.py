from django.shortcuts import render #we dont work here in the default django we will working on the api
from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

# Create your views here.
