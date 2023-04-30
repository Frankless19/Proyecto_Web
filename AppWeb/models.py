from django.db import models

# Creacion de la clase equipo

class Equipo(models.Model):
    nserie = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)
    fechaAdquisicion = models.DateField()
    fechaPuestaMarcha = models.DateField()
    provNombre = models.CharField(max_length=30)
    provTelefono = models.IntegerField(default=0)
    planta = models.CharField(max_length=15)

    # Devuelve un string con la marca, el modelo, y el numero de serie de cada Equipo creado.
    def __str__(self):
        return f" Equipo: {self.marca} {self.modelo}. Numero de serie: {self.nserie}"


# Creacion de la clase Ticket
class Ticket(models.Model):
    nref = models.CharField(max_length = 20)
    titulo = models.CharField(max_length = 10)
    descripcion = models.CharField(max_length = 50)
    fechaApertura = models.DateField()
    fechaResolucion = models.DateField()
    nivelUrgencia = models.ForeignKey('NivelUrgencia', on_delete=models.CASCADE) # relación one-to-many para seleccionar el nivel de urgencia
    tipo = models.ForeignKey('TipoTicket', on_delete=models.CASCADE) # relación one-to-many para seleccionar el tipo de ticket
    estado = models.ForeignKey('EstadoTicket', on_delete=models.CASCADE) # relación one-to-many para seleccionar el estado del ticket
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, default="") # relación one-to-many, un ticket solo es atendido por un empleado
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE, default="") # relación one-to-many, un ticket solo puede tener un equipo
    comentarios = models.CharField(max_length = 40)
    
    #Devuelve un string con la referencia, el titulo, y la descripcion de cada Equipo creado.
    def __str__(self):
        return f" Referencia: {self.nref}. Titulo: {self.titulo}. Descripcion: {self.descripcion}"

# Creacion de la clase Empleado


class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    telefono = models.IntegerField(default=0)

    # Devuelve un string con el nombre, apellido y DNI del empleado

    def __str__(self):
        return f" Nombre: {self.nombre}. {self.apellidos}. Dni: {self.dni}"

class NivelUrgencia(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return f" Nivel: {self.nombre}"

class TipoTicket(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return f" Tipo: {self.nombre}"
    
class EstadoTicket(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return f" Estado: {self.nombre}"