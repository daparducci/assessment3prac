from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish

# Create your views here.
def home(request):
    wishes = Wish.objects.all()
    print(wishes)
    return render(request, 'home.html', {'wishes': wishes})



class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'

class WishDelete(DeleteView):
    model = Wish
    success_url = '/'

 
    