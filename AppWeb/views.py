from typing import Any, Dict
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Empleado, Equipo, Ticket
from .forms import FormEmpleado, FormTicket, FormEquipo
from http.client import HTTPResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q

#Vistas para listar
#class ListaEmpleado(ListView):
    #model = Empleado
    #template_name = 'listadoEmpleados.html'

class ListaEmpleado(ListView):
    model = Empleado
    template_name = 'listadoEmpleados.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("buscar")

        if busqueda:
            queryset = queryset.filter(
                Q(dni__icontains=busqueda) |
                Q(nombre__icontains=busqueda) |
                Q(apellidos__icontains=busqueda)
            ).distinct()

        return queryset
    
class ListaEquipo(ListView):
    model = Equipo
    template_name = 'listadoEquipos.html'
    context_object_name = 'equipos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("buscar")

        if busqueda:
            queryset = queryset.filter(
                Q(nserie__icontains=busqueda) |
                Q(modelo__icontains=busqueda) |
                Q(marca__icontains=busqueda)
            ).distinct()

        return queryset
    
class ListaTicket(ListView):
    model = Ticket
    template_name = 'listadoTickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("buscar")

        if busqueda:
            queryset = queryset.filter(
                Q(nref__icontains=busqueda) |
                Q(titulo__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            ).distinct()

        return queryset

#Vistas para Crear objetos    
class CrearEmpleado(CreateView):
    form_class = FormEmpleado
    template_name = 'creaEmpleado.html'
    model = Empleado
    success_url = reverse_lazy('gestion:listado-empleado')

class CrearEquipo(CreateView):
    form_class = FormEquipo
    template_name = 'creaEquipo.html'
    model = Equipo
    success_url = reverse_lazy('gestion:listado-equipo')

class CrearTicket(CreateView):
    form_class = FormTicket
    template_name = 'creaTicket.html'
    model = Ticket
    success_url = reverse_lazy('gestion:listado-ticket')

#Vistas para borrar
class BorrarEmpleado(DeleteView):
    template_name = 'borrarEmpleado.html'
    model = Empleado
    success_url = reverse_lazy('gestion:listado-empleado')
    
class BorrarEquipo(DeleteView):
    template_name = 'borrarEquipo.html'
    model = Equipo
    success_url  = reverse_lazy('gestion:listado-equipo')
    
class BorrarTicket(DeleteView):
    template_name = 'borrarTicket.html'
    model = Ticket
    success_url = reverse_lazy('gestion:listado-ticket')
    
#Vistas para modificar
class ModificarEmpleado(UpdateView):
    form_class = FormEmpleado
    template_name = 'creaEmpleado.html'
    model = Empleado
    success_url = reverse_lazy('gestion:listado-empleado')

class ModificarEquipo(UpdateView):
    form_class = FormEquipo
    template_name = 'creaEquipo.html'
    model = Equipo
    success_url = reverse_lazy('gestion:listado-equipo')

class ModificarTicket(UpdateView):
    form_class = FormTicket
    template_name = 'creaTicket.html'
    model = Ticket
    success_url = reverse_lazy('gestion:listado-ticket')

#Vistas para los formularios
def post_form(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dni = request.POST["dni"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]   
    return HttpResponse(f"Se ha registrado a {nombre} {apellido} con DNI {dni}")  

#Vistas para mostrar en detalle
class DetalleEmpleado(DetailView):
    template_name = 'detalleEmpleado.html'
    model = Empleado

    #def get_context_data(self, **kwargs): 
        #context super(Show_empleado, self).get_context_data(**kwargs)
        #context['titulo pagina'] = 'detalles del empleado'
        #return context

class DetalleEmpleado(DetailView):
    template_name = 'detalleEmpleado.html'
    model = Empleado

class DetalleEmpleado(DetailView):
    template_name = 'detalleEmpleado.html'
    model = Empleado

#def show_empleado(request, empleado_id):
    #empleado = get_object_or_404(Empleado, pk=empleado_id)
    #context = {'empleado': empleado}
    #return render(request, 'detalleEmpleado.html', context)

class DetalleEquipo(DetailView):
    template_name = 'detalleEquipo.html'
    model = Equipo

class DetalleTicket(DetailView):
    template_name = 'detalleTicket.html'
    model = Ticket

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
