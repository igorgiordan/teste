from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views 

app_name='mercadolivre'

urlpatterns = [
	path('', views.Home.as_view(), name="home"),
    path('cadastro/', views.RegisterUser.as_view(), name="cadastro"),
    path('cadastro-produto/', views.CreateProduto.as_view(), name='cadastro-produto'),
    path('produtos/<pk>/', views.ExibirProduto.as_view(), name='exibir-produto'),
    path('lances/<pk>/', views.AllLances.as_view(), name='lances'),
    path('comprados/', views.Bought.as_view(), name='comprados'),
]