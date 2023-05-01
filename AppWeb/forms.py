from django.forms import ModelForm
from django import forms
from .models import Ticket, Empleado, Equipo, NivelUrgencia, TipoTicket, EstadoTicket


# Formulario asociado a la clase Equipo
class FormEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'nserie': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'fechaAdquisicion': forms.DateInput(attrs={'class':'form-control'}),
            'fechaPuestaMarcha': forms.DateInput(attrs={'class':'form-control'}),
            'provNombre': forms.TextInput(attrs={'class':'form-control'}),
            'provTelefono': forms.NumberInput(attrs={'class':'form-control'}),
            'planta': forms.TextInput(attrs={'class':'form-control'}),
        }

# Formulario asociado a la clase Ticket
class FormTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'nref': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaApertura': forms.DateInput(attrs={'class': 'form-control'}),
            'fechaResolucion': forms.DateInput(attrs={'class': 'form-control'}),
            'nivelUrgencia': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'equipo': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={'class': 'form-control'}),
            
        }


# Formulario asociado a la clase Empleado
class FormEmpleado(ModelForm):
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



    