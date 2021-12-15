#from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import generic

from .models import Task
class HomePageView ( ListView ):
  model = Task
  template_name = 'home.html'

class CreateView ( CreateView ):
    model = Task
    template_name = 'new_task.html'
    fields = '__all__'

class UpdateView ( UpdateView ):
    model = Task
    template_name = 'edit_task.html'
    fields = ['title','body']

class DeleteView ( DeleteView ):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy ( 'home' )