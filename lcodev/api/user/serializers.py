from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.hashers import make_password #this basically bring your pass in a clear text or plain text fromat, hashes it means unreadable format
from rest_framework.decorators import authentication_classes, permission_classes

from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data) #instance interacting with the model and saving its based on it

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr,value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value) #update method not just working for the pass its working for all
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        extra_kwargs = {'password' : {'write_only':True}}
        #here all fields are not from our side, we inheritance some things from other things so we need to add that also here
        fields = ('name', 'email', 'password', 'phone', 'gender',
                  'is_active', 'is_staff', 'is_superuser')
