from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Empleado, Equipo, Ticket
from .forms import FormEmpleado, FormTicket, FormEquipo
from http.client import HTTPResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib import messages

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
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEmpleados'

class CrearEquipo(CreateView):
    form_class = FormEquipo
    template_name = 'creaEquipo.html'
    queryset = Equipo
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEquipos'

class CrearTicket(CreateView):
    form_class = FormTicket
    template_name = 'creaTicket.html'
    queryset = Ticket
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoTickets'

#Vistas para borrar
class BorrarEmpleado(DeleteView):
    template_name = 'borrarEmpleado.html'
    model = Empleado
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEmpleados'
    
class BorrarEquipo(DeleteView):
    template_name = 'borrarEquipo.html'
    model = Equipo
    success_url  = 'http://127.0.0.1:8000/AppWeb/listadoEquipos'
    
class BorrarTicket(DeleteView):
    template_name = 'borrarTicket.html'
    model = Ticket
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoTickets'
    
#Vistas para modificar
class ModificarEmpleado(UpdateView):
    form_class = FormEmpleado
    template_name = 'creaEmpleado.html'
    model = Empleado
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEmpleados'

class ModificarEquipo(UpdateView):
    form_class = FormEquipo
    template_name = 'creaEquipo.html'
    model = Equipo
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoEquipos'

class ModificarTicket(UpdateView):
    form_class = FormTicket
    template_name = 'creaTicket.html'
    model = Ticket
    success_url = 'http://127.0.0.1:8000/AppWeb/listadoTickets'

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

def show_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    context = {'equipo': equipo}
    return render(request, 'detalleEquipo.html', context)

def show_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {'ticket': ticket}
    return render(request, 'detalleTicket.html', context)

#Vista de login
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login (request,user)
            return redirect('/AppWeb/listadoEmpleados')
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')
    context = {}
    return render(request, 'login.html', context)
