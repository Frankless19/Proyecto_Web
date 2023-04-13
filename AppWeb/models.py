from django.db import models

# Creacion de la clase equipo


class Equipo(models.Model):
    nserie = models.CharField.primary_key(max_length=20)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    tipoEquipo = models.CharField(max_length=20)
    fechaAdquisicion = models.DateTimeField()
    fechaPuestaMarcha = models.DateTimeField()
    provNombre = models.CharField(max_length=30)
    provTelefono = models.IntegerField(default=0)
    planta = models.CharField(max_length=15)

    # Devuelve un string con la marca, el modelo, y el numero de serie de cada Equipo creado.
    def __str__(self):
        return f" Equipo: {self.marca} {self.modelo}. Numero de serie: {self.nserie}"


# Creacion de la clase Ticket
class Ticket(models.Model):
<<<<<<< HEAD
    nref = models.CharField.primary_key(max_length = 20)
    titulo = models.CharField(max_length = 10)
    descripcion = models.CharField(max_length = 50)
    fechaApertura = models.DateTimeField()
    fechaResolucion = models.DateTimeField()
    nivelUrgencia = models.(max_length = 5)
    tipoTicket = models.(max_length = 15)
    estadoTicket = models.BooleanField()
    empleadoticket = models.CharField(max_length = 15)
    cometarios = models.CharField(max_length = 40)
    
    #Devuelve un string con la referencia, el titulo, y la descripcion de cada Equipo creado.
=======
    nref = models.CharField.primary_key(max_length=20)
    Titulo = models.CharField(max_length=10)
    Descripcion = models.CharField(max_length=50)
    FechaApertura = models.DateTimeField()
    FechaResolucion = models.DateTimeField()
    NivelUrgencia = models.(max_length=5)
    TipoTicket = models.(max_length=15)
    EstadoTicket = models.BooleanField()
    Empleadoticket = models.CharField(max_length=15)
    Cometarios = models.CharField(max_length=40)

    # Devuelve un string con la marca, el modelo, y el numero de serie de cada Equipo creado.
>>>>>>> 6abc8c829a58d8282215f4fe733ba19bd63f3229
    def __str__(self):
        return f" Referencia: {self.nref}. Titulo: {self.Titulo}. Descripcion: {self.Descripcion}"

# Creacion de la clase Empleado


class Empleado(models.Model):
    dni = models.CharField.primary_key(max_length=9)
    nombre = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    telefono = models.IntegerField(default=0)

    # Devuelve un string con el nombre, apellido y DNI del empleado

    def __str__(self):
        return f" Nombre: {self.nombre}. {self.apellidos}. Descripcion: {self.dni}"
