from django.shortcuts import render
from django.views.generic import ListView

from .models import Website

class HomeIndex(ListView):
    model = Website
    template_name = 'core/index.html'
    context_object_name = 'urls'