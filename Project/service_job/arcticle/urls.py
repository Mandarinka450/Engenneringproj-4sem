from django.urls import path

from . import views


urlpatterns = [
    path('arcticles/', views.index, name='arcticle'),
]
