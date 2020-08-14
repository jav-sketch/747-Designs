from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import *
# Create your views here.

# def index(request):
#     return render(request, "index.html")
    

class HomeView(View):
    model = Customer
    template_name = "index.html"