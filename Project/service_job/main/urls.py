from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('vacancies', views.index2, name='vacancies'),
    path('reviews', views.index3, name='reviews'),
    path('adreview', views.create_view, name='adreview'),
    path('reviews/<id_review>/update', views.update_view, name='review_update'),
    path('reviews/<id_review>/delete', views.delete_view, name='review_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('arcticle/', include('arcticle.urls')),


]
