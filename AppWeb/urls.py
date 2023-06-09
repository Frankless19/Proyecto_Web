from django.urls import path
from . import views
from AppWeb import views

# Esta variable app_name sirve para que Django pueda diferenciar las URL de cada proyecto
app_name = 'gestion'

urlpatterns = [
    path('AppWeb/listadoEmpleados/', views.ListaEmpleado.as_view(), name='listado-empleado'),
    path('AppWeb/listadoEquipos/', views.ListaEquipo.as_view(), name='listado-equipo'),
    path('AppWeb/listadoTickets/', views.ListaTicket.as_view(), name='listado-ticket'),
    
    path('AppWeb/creaEmpleado/',views.CrearEmpleado.as_view(), name='crear-empleado'),
    path('AppWeb/creaEquipo/',views.CrearEquipo.as_view(), name='crear-equipo'),
    path('AppWeb/creaTicket/',views.CrearTicket.as_view(), name='crear-ticket'),
    
    path('AppWeb/borrarEmpleado/<int:pk>/',views.BorrarEmpleado.as_view(), name='borrar-empleado'),
    path('AppWeb/borrarEquipo/<int:pk>/',views.BorrarEquipo.as_view(), name='borrar-equipo'),
    path('AppWeb/borrarTicket/<int:pk>/',views.BorrarTicket.as_view(), name='borrar-ticket'),
    
    path('AppWeb/modificarEmpleado/<int:pk>/',views.ModificarEmpleado.as_view(), name='modificar-empleado'),
    path('AppWeb/modificarEquipo/<int:pk>/',views.ModificarEquipo.as_view(), name='modificar-equipo'),
    path('AppWeb/modificarTicket/<int:pk>/',views.ModificarTicket.as_view(), name='modificar-ticket'),
    
    path('AppWeb/listadoEmpleados/<int:pk>',views.DetalleEmpleado.as_view(), name='detalle-empleado'),
    path('AppWeb/listadoEquipos/<int:pk>',views.DetalleEquipo.as_view(), name='detalle-equipo'),
    path('AppWeb/listadoTickets/<int:pk>',views.DetalleTicket.as_view(), name='detalle-ticket'),
    
    path('', views.loginPage, name="login"),
    path('', views.logoutUser, name="logout"),

    path('apiempleados', views.EmpListView.as_view(), name= 'listaempleados-api'),
    path('apiempleados/<int:pk>', views.EmpDetailView.as_view(), name= 'listaempleado-api'),

    path('apiequipos', views.EquListView.as_view(), name= 'listaequipo-api'),
    path('apiequipos/<int:pk>', views.EquDetailView.as_view(), name= 'listaequipo-api'),

    path('apitickets', views.TicListView.as_view(), name= 'listaticket-api'),
    path('apitickets/<int:pk>', views.TicDetailView.as_view(), name= 'listaticket-api'),
    
]