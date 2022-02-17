from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#validating the user authentication
def validate_user_session(id,token):
    UserModel = get_user_model() #grab usermodel
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token: #here we will check the user model and request (token) are same
            return True
        return False
    except UserModel.DoesNotExist:
        return False
#collecting all the data and pushing that data in the admin
@csrf_exempt #placing this decorator here
def add(request,id,token): #here we have the post request, id and the token
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Please re-login' , 'code':'1'})

    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_pro = len(products.split(',')[:-1]) #we need to check how many total products are there

        UserModel = get_user_model() #grab the user model

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error' : 'User does not exist'})

        ordr = Order(user=user, product_names=products,total_products=total_pro,transaction_id=transaction_id,total_amount=amount) #in the model we will assign all this values
        ordr.save()
        return JsonResponse({'success':True, 'error':False, 'msg':'order placed successfully'})
#add the view set here
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
