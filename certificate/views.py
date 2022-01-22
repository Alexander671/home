from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect #для отображения и редиректа берем необходимые классы
from .models import Certificate #не забываем наши модели
 
from .models import Certificate
from .form import CertificatesForm
from django.db.models import Q


def redirect_view(request):
     	return redirect("/certificate")


def certificate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CertificatesForm(request.POST)
            # прикольчики
            if request.user.username == 'anna' and request.POST["text"] != 'хочу':
                return HttpResponse('Волшебное слово!')
            if form.is_valid():
                certificate = form.save(commit=False)
                certificate.user = request.user
                certificate.save()
                return redirect('/certificate/')
        else:
            form = CertificatesForm()
        certificates = Certificate.objects.filter(Q(user = request.user, accept = 1)) | Certificate.objects.filter(Q(user_with = request.user, accept = 1))
        accept = Certificate.objects.filter(user_with = request.user, accept = False)

        return render(request, 'certificate.html', {'certificates' : certificates, 'form': form, 'accept' : accept, 'user' : request.user})
    else:
        return render(request, "notin.html")
        
def certificate_accept(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if not certificate.accept and request.user == certificate.user_with:
        certificate.accept = True
        certificate.save()
    else:
        return HttpResponse('Вы не можете повлиять на этот сертификат!')
    return redirect('/certificate/')
    

def certificate_delete(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if not certificate.accept and request.user == certificate.user_with or request.user == certificate.user :
        certificate.delete()
    else:
        return HttpResponse('Вы не можете повлиять на этот сертификат!')
    return redirect('/certificate/')

def certificate_use(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if  certificate.amount == 1 and certificate.use_request:
        certificate.delete()
 
    elif not certificate.use_request and request.user == certificate.user_with:
        certificate.use_request = True
        certificate.save()
    elif certificate.use_request and request.user == certificate.user:
        certificate.use_request = False
        certificate.amount -= 1
        certificate.save()

    else:
        return HttpResponse('Вы не можете повлиять на этот сертификат!')
    return redirect('/certificate/')