from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class HomePageView(TemplateView):
  template_name = 'home.html'

class AcercadePageView(TemplateView):
  template_name = 'about.html'