from django.urls import path
from . import views

#urls.py creado en la carpeta persona

urlpatterns = [
    path('',views.home),
    path('registrarPersona/', views.registrarPersona)
    ]