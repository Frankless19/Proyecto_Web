from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Empleado, Equipo, Ticket
# Create your views here.

def index(request):
    return HttpResponse("Bienvenido")

class ListaEmpleado(CreateView, ListView):
    model = Empleado
    template_name = 'listadoEmpleados.html'
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEmpleados/'
    
class ListaEquipo(CreateView, ListView):
    model = Equipo
    template_name = 'listadoEquipos.html'
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEquipos/'
    
class ListaTicket(CreateView, ListView):
    model = Ticket
    template_name = 'listadoTickets.html'
    success_url = 'http://127.0.0.1:8000/appWeb/listadoTickets/'
    
    
