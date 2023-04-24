from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_entrada = models.DateField(null=False)
    fecha_salida = models.DateField(null=False)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100, null=False)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido, self.email, self.edad, self.sexo, self.fecha_nacimiento, self.fecha_entrada, self.fecha_salida, self.direccion, self.telefono)
    
     