from django.urls import path
from .views import *
urlpatterns=[
    path('',Index),
    path('about/',About_as),
    path('shop/',Shop),
    path('contact',Contact),
    path('send/',Send)
]