from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoa/nova/', views.pessoa_nova, name='pessoa_nova'),
    path('pessoa/update/<int:id>/', views.pessoa_update, name='pessoa_update'),
    path('pessoa/delete/<int:id>/', views.pessoa_delete, name='pessoa_delete'),
]