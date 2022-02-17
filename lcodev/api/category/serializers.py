from rest_framework import serializers
from .models import Category #from model.py

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')