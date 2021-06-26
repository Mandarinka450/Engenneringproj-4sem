from django.urls import path
from .views import ServicesView


app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('services/', ServicesView.as_view()),
    path('services/<int:pk>', ServicesView.as_view())
]
