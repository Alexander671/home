from django.utils import timezone #мы будем получать дату создания todo
from django.db import models
from django.contrib.auth.models import User


class Certificate(models.Model):
    name = models.CharField(max_length=250)
    amount = models.PositiveSmallIntegerField() 
    use_request = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # дата создания
    user =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    user_with = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True)
    accept = models.BooleanField(default = False)
    
    class Meta: #используем вспомогательный класс мета для сортировки наших дел
        ordering = ["-created"] #сортировка дел по времени их создания
    def __str__(self):
    	return self.name 