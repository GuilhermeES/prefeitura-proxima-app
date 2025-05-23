"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.home, name='home'),
    path('novo-chamado/', views.novo_chamado, name='novo_chamado'),
    path('ver-chamado/<int:chamado_id>/', views.ver_chamado, name='ver_chamado'),
    path('editar-chamado/<int:chamado_id>/', views.editar_chamado, name='editar_chamado'),
    path('excluir-chamado/<int:chamado_id>/', views.excluir_chamado, name='excluir_chamado'),
]
