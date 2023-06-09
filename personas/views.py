from django.shortcuts import render, redirect
from .models import Persona


# Create your views here.
def home(request):
    #return render(request,"bienvenida.html")
    personas = Persona.objects.all()
    return render(request,"listar.html", {"personas":personas})

def registrarPersona(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    edad = request.POST['edad']
    sexo = request.POST['sexo']
    fecha_nacimiento = request.POST['fecha_nacimiento']
    fecha_entrada = request.POST['fecha_entrada']
    fecha_salida = request.POST['fecha_salida']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']

    persona=Persona.objects.create(nombre=nombre, apellido=apellido, email=email, edad=edad, sexo=sexo, fecha_nacimiento=fecha_nacimiento, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida, direccion=direccion, telefono=telefono)

    return redirect('/')

def editarPersona(request, id):
    persona = Persona.objects.get(id=id)
    return render(request, 'persona.html', {'persona':persona})

def editPersona(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    edad = request.POST['edad']
    sexo = request.POST['sexo']
    fecha_nacimiento = request.POST['fecha_nacimiento']
    fecha_entrada = request.POST['fecha_entrada']
    fecha_salida = request.POST['fecha_salida']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']

    persona = Persona.objects.get(id=id)
    persona.nombre = nombre
    persona.apellido = apellido
    persona.email = email
    persona.edad = edad
    persona.sexo = sexo
    persona.fecha_nacimiento = fecha_nacimiento
    persona.fecha_entrada = fecha_entrada
    persona.fecha_salida = fecha_salida
    persona.direccion = direccion
    persona.telefono = telefono

    persona.save()

    return redirect('/')




def eliminarPersona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()

    return redirect('/')