from django.urls import path
# from .views import *
from . import views




app_name = 'Design_Site'
urlpatterns = [
    path('', views.index, name='index')
    # path('', Home.as_view(), name='home')
]
