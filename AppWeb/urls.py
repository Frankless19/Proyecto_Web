from django.urls import path
from . import views
from .views import ListaEmpleado, ListaEquipo, ListaTicket, CrearEmpleado, BorrarEmpleado, CrearEquipo
from AppWeb import views

# Esta variable app_name sirve para que Django pueda diferenciar las URL de cada proyecto
app_name = 'gestion'

urlpatterns = [
    path('AppWeb/listadoEmpleados/', ListaEmpleado.as_view(), name='listado-empleado'),
    path('AppWeb/listadoEquipos/', ListaEquipo.as_view(), name='listado-equipo'),
    path('AppWeb/listadoTicket/', ListaTicket.as_view(), name='listado-ticket'),
    
    path('AppWeb/creaEmpleado/',CrearEmpleado.as_view(), name='crear-empleado'),
    path('AppWeb/creaEquipo/',CrearEquipo.as_view(), name='crear-equipo'),
    path('AppWeb/creaEquipo/',CrearEquipo.as_view(), name='crear-ticket'),
    
    path('AppWeb/borrarEmpleado/<int:pk>/',BorrarEmpleado.as_view(), name='borrar-empleado'),
    
    path('AppWeb/registrado/',views.post_form, name='empleado-registrado'),

    #path('AppWeb/listadoEmpleados/<int:empleado_id>',views.show_empleado(), name='detalle-empleado'),
    
]