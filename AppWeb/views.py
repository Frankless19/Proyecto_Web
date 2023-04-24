from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Empleado, Equipo, Ticket
from .forms import FormEmpleado, FormTicket, FormEquipo
from http.client import HTTPResponse

#Vistas para listar
class ListaEmpleado(ListView):
    model = Empleado
    template_name = 'listadoEmpleados.html'
    
class ListaEquipo(ListView):
    model = Equipo
    template_name = 'listadoEquipos.html'
    
class ListaTicket(ListView):
    model = Ticket
    template_name = 'listadoTickets.html'

#Vistas para Crear objetos    
class CrearEmpleado(CreateView):
    form_class = FormEmpleado
    template_name = 'creaEmpleado.html'
    queryset = Empleado

class CrearEquipo(CreateView):
    form_class = FormEquipo
    template_name = 'creaEquipo.html'
    queryset = Equipo
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEquipos'

#Vistas para borrar
class BorrarEmpleado(DeleteView):
    template_name = 'borrarEmpleado.html'
    model = Empleado
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEmpleados'

#Vistas para los formularios
def post_form(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dni = request.POST["dni"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]   
    return HttpResponse(f"Se ha registrado a {nombre} {apellido} con DNI {dni}")  

#Vistas para mostrar en detalle

def show_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    context = {'empleado': empleado}
    return render(request, 'detalleEmpleado.html', context)

