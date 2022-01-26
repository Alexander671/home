from django.utils import timezone, dateformat
from django.db import models
from django.conf import settings



class Request(models.Model): # Таблица новостей которая наследует models.Model
    url = models.TextField() # название тега
    time_request = models.DateTimeField(default = timezone.now().replace(second=0, microsecond=0)) # дата создания
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True, null = True)
    response = models.TextField(null =  True)
    description = models.CharField(max_length = 300, null = True)
    class Meta:
        verbose_name = ("Request") # человекочитаемое имя объекта
        verbose_name_plural = ("Requests")  #человекочитаемое множественное имя для Категорий
    def __str__(self):
        return self.url  # __str__ применяется для отображения объекта в интерфейсе