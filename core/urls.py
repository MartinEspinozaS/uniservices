from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('lista_servicios/',views.lista_servicios, name='lista_servicios'),
    path('infoservice/', views.infoservice, name='infoservice'),
    path('lista_campus/', views.lista_campus, name='lista_campus'),
    path('lista_departamento/', views.lista_departamento, name='lista_departamento'),
]