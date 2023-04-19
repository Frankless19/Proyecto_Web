from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Empleado, Equipo, Ticket
# Create your views here.

class ListaEmpleado(ListView):
    model = Empleado
    template_name = 'listadoEmpleados.html'
    
class ListaEquipo(ListView):
    model = Equipo
    template_name = 'listadoEquipos.html'
    
class ListaTicket(ListView):
    model = Ticket
    template_name = 'listadoTickets.html'
    
    
