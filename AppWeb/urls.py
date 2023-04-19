from django.urls import path
from . import views
from .views import ListaEmpleado, ListaEquipo, ListaTicket
from AppWeb import views

# Esta variable app_name sirve para que Django pueda diferenciar las URL de cada proyecto
app_name = 'gestion'

urlpatterns = [
    path('AppWeb/listadoEmpleados/', ListaEmpleado.as_view(), name='listado-empleado'),
    path('AppWeb/listadoEquipos/', ListaEquipo.as_view(), name='listado-equipo'),
    path('AppWeb/listadoTicket/', ListaTicket.as_view(), name='listado-ticket')
]