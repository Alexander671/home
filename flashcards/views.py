from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from flashcards.models import Category, FlashCard
from .form import FlashCardForm, CategoryForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from math import ceil
class FlashCardView(TemplateView):
    def get(self, request, *args, **kwargs):
        cards = FlashCard.objects.all()
        paginator = Paginator(cards, 20)
        length = ceil(len(cards) / 20)

        formcard = FlashCardForm()
        formcategory = CategoryForm()

        page = request.GET.get('page')  
        page_2 = request.GET.get('page_2')
        
        try:  
            cards = paginator.page(page)  
            paginator_2 = Paginator(cards, 1)
            cards_2 = paginator_2.page(page_2)
        except PageNotAnInteger:  
            # Если страница не является целым числом, поставим первую страницу  
            cards = paginator.page(1)
            paginator_2 = Paginator(cards, 1)
            cards_2 = paginator_2.page(1)  
        except EmptyPage:  
            # Если страница больше максимальной, доставить последнюю страницу результатов  
            cards = paginator.page(paginator.num_pages)  
        return render(request, 'flashcard.html', {'formcard' : formcard, 'formcategory': formcategory, 'page' : int(page),  'cards_2': cards_2, 'length' : range(1, length + 1)})

    def post(self, request):
        formcard = FlashCardForm(request.POST)
        formcategory = CategoryForm(request.POST)
        
        if formcard.is_valid():
            
            req = formcard.save(commit=False)
            req.user = request.user
            req.save()
        
        if formcategory.is_valid():
            
            req = formcategory.save(commit=False)
            req.user = request.user
            req.save()
            
        return redirect('/flashcards/')
