from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('login/', views.signin, name='signin'),#this is custom path
    path('logout/<int:id>/', views.signout, name='signout'), #same custom path, id will capture via url thats why we gave <int:id>
    path('', include(router.urls))
]