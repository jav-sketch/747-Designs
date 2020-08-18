from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .models import *
# Create your views here.

def index(request):
    return render(request, "index.html")
    

# class Home(View):
#     model = Customer
#     template_name = "index.html"