from django.shortcuts import render
from django.views.generic import *

# Create your views here.

class Home(TemplateView):

    template_name = "index.html"


class SecondPage(TemplateView):
    template_name = "secondPage.html"

class TreePage(TemplateView):
    template_name = "tree.html"