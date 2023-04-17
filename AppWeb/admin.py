from django.contrib import admin
from .models import Equipo, Empleado, Ticket, NivelUrgencia, TipoTicket, EstadoTicket

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Empleado)
admin.site.register(Ticket)
admin.site.register(NivelUrgencia)
admin.site.register(TipoTicket)
admin.site.register(EstadoTicket)