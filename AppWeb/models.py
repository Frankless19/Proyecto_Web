from django.db import models

#Creacion de la clase equipo
class Equipo(models.Model):
    nserie = models.CharField.primary_key(max_length = 20)
    modelo = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 30)
    tipoEquipo = models.CharField(max_length = 20)
    fechaAdquisicion = models.DateTimeField()
    fechaPuestaMarcha = models.DateTimeField()    
    provNombre = models.CharField(max_length = 30)
    provTelefono = models.IntegerField(default= 0)
    planta = models.CharField(max_length = 15)
    
    #Devuelve un string con la marca, el modelo, y el numero de serie de cada Equipo creado.
    def __str__(self):
        return f" Equipo: {self.marca} {self.modelo}. Numero de serie: {self.nserie}"
    