from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import *
# Create your views here.


# def index(request):
#     return render(request, "index.html")


class HomeView(TemplateView):
    template_name = "index.html"