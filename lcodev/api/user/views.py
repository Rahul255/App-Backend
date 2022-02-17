
from django.contrib.auth.models import User #this is the usermodel
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.fields import REGEX_TYPE
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse, request
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt #django also provide this
from django.contrib.auth import login, logout #default login and logout
import random
import re #its  used for running the regular expression

# Create your views here.


# this for generating session token
def generate_session_token(length=10):
    # this underscore is empty variable
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)])for _ in range(10))


# signin portion
@csrf_exempt #we will signup from another origin request
#somebody definitely make a request for this
def signin(request):
    if not request.method == 'POST': #verify the request is post or not
        return JsonResponse({'error': 'Send a post request with valid parameter only'})

    username = request.POST['email'] #we will take this as email from the user
    password = request.POST['password'] #its same password from the user

    # validation part
    #its match with username
    if not re.match("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'password needs to be atleast of 3 char'})

    UserModel = get_user_model() #model grabs from the authentication

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            #user dictionary
            usr_dict = UserModel.objects.filter(
                email=username).values().first() #that email value takes first
            usr_dict.pop('password') #simply grab the password

            #need to work on the token, this all are default django method
            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': "previous session exists"})

            token = generate_session_token() #we need to generate the token
            user.session_token = token
            user.save() #token is now saved into the user
            login(request, user) #now use the default django login, login need two thing the request and user
            return JsonResponse({'token': token, 'user': usr_dict}) #thorw the same token and user dictionary
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})


# signout portion
#here we will sent a request and also provide one id, the id will capture via the url
def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid User ID'})

    return JsonResponse({'success': 'Logout success'})

# viewset


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    #how we can grab the permission
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
