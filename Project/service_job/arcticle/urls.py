from django.urls import path

from .views import ArticlesView


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticlesView.as_view()),
    path('articles/<int:pk>', ArticlesView.as_view())
]
