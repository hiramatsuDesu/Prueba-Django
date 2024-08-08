from django import forms
from .models import Persona

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    mail = forms.EmailField(max_length=100)
    

class PersonaModelForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'