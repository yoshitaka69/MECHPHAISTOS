from django.shortcuts import render
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'jobs/index.html'

# Create your views here.
