from django.forms import ModelForm
from django import forms
from .models import Ticket, Empleado, EstadoTicket, NivelUrgencia, TipoTicket, Equipo

# Formulario asociado a la clase Equipo
class Equipo(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'nserie': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'tipo': forms.NumberInput(attrs={'class':'form-control'}),
            'fechaAdquisicion': forms.DateTimeInput(attrs={'class':'form-control'}),
            'fechaPuestaMarcha': forms.DateTimeInput(attrs={'class':'form-control'}),
            'provNombre': forms.TextInput(attrs={'class':'form-control'}),
            'provTelefono': forms.NumberInput(attrs={'class':'form-control'}),
            'planta': forms.TextInput(attrs={'class':'form-control'}),
        }

         # Formulario asociado a la clase Ticket
class Ticket(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'nref': forms.TextInput(attrs={'class':'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'fechaApertura': forms.DateTimeInput(attrs={'class':'form-control'}),
            'fechaResolucion': forms.DateTimeInput(attrs={'class':'form-control'}),
            'nivelUrgencia': forms.NumberInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'empleado': forms.TextInput(attrs={'class':'form-control'}),
            'equipo': forms.TextInput(attrs={'class':'form-control'}),
            'cometarios': forms.TextInput(attrs={'class':'form-control'}),
        }

# Formulario asociado a la clase Empleado
class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
        }

# Formulario asociado a la clase NivelUrgencia
class NivelUrgencia(ModelForm):
    class Meta:
        model = NivelUrgencia
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }

     # Formulario asociado a la clase TipoTicket
class NivelUrgencia(ModelForm):
    class Meta:
        model = TipoTicket
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }

        # Formulario asociado a la clase EstadoTicket
class NivelUrgencia(ModelForm):
    class Meta:
        model = EstadoTicket
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }

    