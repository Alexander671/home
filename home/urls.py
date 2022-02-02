
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from django.urls import re_path

from todo.views import todo
from todo.views import category
from certificate.views import certificate, certificate_accept, certificate_delete, certificate_use

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('iot/', include('iot.urls')),
    path('flashcards/', include('flashcards.urls')),
	
    path('certificate/<int:pk>/accept', certificate_accept, name = 'certificate_accept'),
    path('certificate/<int:pk>/delete', certificate_delete, name = 'certificate_delete'),
    path('certificate/<int:pk>/use', certificate_use, name = 'certificate_use'),
 	
    re_path('todo/', todo, name="Todo"),
	re_path('category/', category, name="Category"),
    re_path('certificate/', certificate, name = 'Certificate'),
] 