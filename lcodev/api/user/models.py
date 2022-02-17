from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#this is inherit from the abstract user
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=255, unique=True) #user login based on the email and pass

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #now its an empty array

    #maybe you want create more field you can add here

    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    #this is our custom token
    session_token = models.CharField(max_length=10,default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)