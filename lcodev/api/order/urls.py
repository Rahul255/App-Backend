from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet),

urlpatterns = [
    #here need to add the add path
    path('add/<str:id>/<str:token>/', views.add, name='order.add'),#id,and token comming from string format
    path('', include(router.urls))
]