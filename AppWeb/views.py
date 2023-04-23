from django.shortcuts import render
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
    
#Vistas para los formularios
def post_form(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dni = request.POST["dni"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]   
    return HttpResponse(f"Se ha registrado a {nombre} {apellido} con DNI {dni}")    
    