from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from flashcards.models import Category, FlashCard
from .form import FlashCardForm, CategoryForm
class FlashCardView(TemplateView):
    def get(self, request, *args, **kwargs):
        formcard = FlashCardForm()
        formcategory = CategoryForm()
        return render(request, 'flashcard.html', {'formcard' : formcard, 'formcategory': formcategory})
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
