from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vacancies', views.index2, name='vacancies'),
]
