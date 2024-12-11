
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('index2/',home2,name='index2')
]
