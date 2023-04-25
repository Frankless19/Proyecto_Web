from django.forms import ModelForm
from django import forms
from .models import Ticket, Empleado, Equipo

# Formulario asociado a la clase Equipo
class FormEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'nserie': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'fechaAdquisicion': forms.DateTimeInput(attrs={'class':'form-control'}),
            'fechaPuestaMarcha': forms.DateTimeInput(attrs={'class':'form-control'}),
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
            'nref': forms.TextInput(attrs={'class':'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'fechaApertura': forms.DateTimeInput(attrs={'class':'form-control'}),
            'fechaResolucion': forms.DateTimeInput(attrs={'class':'form-control'}),
            #'nivelUrgencia': forms.ModelChoiceField(attrs={'class':'form-control'}),
            #'tipo': forms.ChoiceField(attrs={'class':'form-control'}),
            #'estado': forms.ChoiceField(attrs={'class':'form-control'}),
            #'empleado': forms.ChoiceField(attrs={'class':'form-control'}),
            #'equipo': forms.ChoiceField(attrs={'class':'form-control'}),
            'cometarios': forms.TextInput(attrs={'class':'form-control'}),
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



    