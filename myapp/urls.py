from django.conf.urls import url, include
from .views import *
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register(r'item', ItemOverViewViewSet)
router.register(r'itemrequest', ItemRequestViewSet)

urlpatterns = [
   
    url(r'^', include(router.urls )),
    path('current_user/', get_current_user),
    path('users/create', CreateUserView.as_view()),
 
]