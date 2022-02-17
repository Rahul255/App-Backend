from django.shortcuts import render
# JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response. Its default Content-Type header is set to application/json. The first parameter, data , should be a dict instance.
from django.http import JsonResponse

# Create your views here.


# this view for the home
# request - what you are expecting here actually we will expect some request
def home(request):
    return JsonResponse({'info': 'django react course', 'name': 'rahul'})
