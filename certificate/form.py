from django.forms import ModelForm
from .models import Certificate

class CertificatesForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['name','user_with', 'amount']