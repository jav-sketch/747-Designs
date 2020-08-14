from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', HomeView.as_view(), name='index')
]
