from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoa/nova/', views.pessoa_nova, name='pessoa_nova'),
]