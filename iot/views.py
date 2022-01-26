from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from requests import get

from iot.form import RequestForm
from .models import Request

class SocketView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = RequestForm()
        schedule = Request.objects.filter(user_id=request.user.id)
        return render(request, 'iot.html', {'schedule' : schedule, 'formset' : form})
    
    def post(self, request):
        form = RequestForm(request.POST)
        if form.is_valid():
            
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            
        return render(request, 'iot.html', {'formset': form})



def onView(request):
    get('http://192.168.2.7/LED=OFF')
    return redirect('iot')

def offView(request):
    get('http://192.168.2.7/LED=ON')
    return redirect('iot')
    
 
    