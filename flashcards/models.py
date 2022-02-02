from django.utils import timezone, dateformat
from django.db import models
from django.conf import settings



class Category(models.Model):
    category = models.CharField(max_length=300)
    def __str__(self):
        return self.category
class FlashCard(models.Model): # Таблица новостей которая наследует models.Model
    question = models.TextField() # название тега
    answer = models.TextField() # название тега
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True, null = True)
    category = models.ForeignKey(Category, default="general",on_delete=models.PROTECT)
    class Meta:
        verbose_name = ("FlashCard") # человекочитаемое имя объекта
        verbose_name_plural = ("FlashCards")  #человекочитаемое множественное имя для Категорий
    def __str__(self):
        return self.url  # __str__ применяется для отображения объекта в интерфейсе

