from django.urls import path
from . import views
from .views import ListaEmpleado, ListaEquipo, ListaTicket, CrearEmpleado, BorrarEmpleado, CrearEquipo, BorrarEquipo, ModificarEmpleado, ModificarEquipo, BorrarTicket, ModificarTicket, CrearTicket
from AppWeb import views

# Esta variable app_name sirve para que Django pueda diferenciar las URL de cada proyecto
app_name = 'gestion'

urlpatterns = [
    path('AppWeb/listadoEmpleados/', ListaEmpleado.as_view(), name='listado-empleado'),
    path('AppWeb/listadoEquipos/', ListaEquipo.as_view(), name='listado-equipo'),
    path('AppWeb/listadoTickets/', ListaTicket.as_view(), name='listado-ticket'),
    
    path('AppWeb/creaEmpleado/',CrearEmpleado.as_view(), name='crear-empleado'),
    path('AppWeb/creaEquipo/',CrearEquipo.as_view(), name='crear-equipo'),
    path('AppWeb/creaTicket/',CrearTicket.as_view(), name='crear-ticket'),
    
    path('AppWeb/borrarEmpleado/<int:pk>/',BorrarEmpleado.as_view(), name='borrar-empleado'),
    path('AppWeb/borrarEquipo/<int:pk>/',BorrarEquipo.as_view(), name='borrar-equipo'),
    path('AppWeb/borrarTicket/<int:pk>/',BorrarTicket.as_view(), name='borrar-ticket'),
    
    path('AppWeb/modificarEmpleado/<int:pk>/',ModificarEmpleado.as_view(), name='modificar-empleado'),
    path('AppWeb/modificarEquipo/<int:pk>/',ModificarEquipo.as_view(), name='modificar-equipo'),
    path('AppWeb/modificarTicket/<int:pk>/',ModificarTicket.as_view(), name='modificar-ticket'),
    
    path('AppWeb/listadoEmpleados/<int:empleado_id>',views.show_empleado, name='detalle-empleado'),
    path('AppWeb/listadoEquipos/<int:equipo_id>',views.show_equipo, name='detalle-equipo'),
    path('AppWeb/listadoTickets/<int:ticket_id>',views.show_ticket, name='detalle-ticket'),
    
    path('', views.loginPage, name="login"),
    
]