from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from flashcards.models import Category, FlashCard
from .form import FlashCardForm, CategoryForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  

class FlashCardView(TemplateView):
    def get(self, request, *args, **kwargs):
        cards = FlashCard.objects.all()
        paginator = Paginator(cards, 1)

        formcard = FlashCardForm()
        formcategory = CategoryForm()
        page = request.GET.get('page')  
        try:  
            cards = paginator.page(page)  
        except PageNotAnInteger:  
            # Если страница не является целым числом, поставим первую страницу  
            cards = paginator.page(1)  
        except EmptyPage:  
            # Если страница больше максимальной, доставить последнюю страницу результатов  
            cards = paginator.page(paginator.num_pages)  
        return render(request, 'flashcard.html', {'formcard' : formcard, 'formcategory': formcategory, 'page' : page, 'cards' : cards})

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
