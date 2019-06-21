from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Skill

# Create your views here.
def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})



class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'
    success_url = '/'

class SkillDelete(DeleteView):
    model = Skill
    success_url = '/'

    # def form_valid(self, form):
    #     print(self)
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
    