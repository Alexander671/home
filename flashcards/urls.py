 
from django.contrib import admin
from django.urls import path
from .views import FlashCardView
urlpatterns = [
    path('', FlashCardView.as_view(), name='iot')
]    
 