from django.urls import path
from .views import *




app_name = 'Design_Site'
urlpatterns = [
    # path('', views.index, name='index')
    path('', HomeView.as_view(), name="index"),

]
