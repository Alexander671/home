 
from django.contrib import admin
from django.urls import path
from .views import SocketView, onView, offView
urlpatterns = [
    path('on/', onView, name='iot'),
    path('', SocketView.as_view(), name='iot'),
    path('off/', offView, name = 'Off')
] 
 
