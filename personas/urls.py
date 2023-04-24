from django.urls import path
from . import views

#urls.py creado en la carpeta persona

urlpatterns = [
    path('',views.home),
    path('registrarPersona/', views.registrarPersona),
    path('editarPersona/<id>', views.editarPersona),
    path('editPersona/', views.editPersona),
    path('eliminarPersona/<id>', views.eliminarPersona),

    ]