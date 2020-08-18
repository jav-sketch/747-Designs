from django.urls import pat
from Design_Site.views import *




app_name = 'Design_Site'
urlpatterns = [
    # path('', views.index, name='index')
    path('', HomeView.as_view(), name="index")
]
