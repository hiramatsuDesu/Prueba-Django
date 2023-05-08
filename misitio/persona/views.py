from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Persona
from .forms import PersonaModelForm


# Create your views here.
def index_persona(request):
    persona_lista = Persona.objects.all()
    context = {
        'persona_lista':persona_lista
    }
    return render(request, 'persona/lista.html', context)

def crearUsuario(request):
    persona_lista = Persona.objects.all()

    form = PersonaModelForm()

    if(request.method == 'POST'):
        print("ha ingresado al metodo post ")

        form = PersonaModelForm(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            print(form.errors)
    context = {
        'form': form,
        'persona_lista':persona_lista
    }
       

    return render(request, 'persona/crear.html', context)


def borrarUsuario(request, pk):
    Persona.objects.get(pk=pk).delete()

    persona_lista = Persona.objects.all()
    context = {
        'persona_lista':persona_lista
    }
    #return render(request, 'persona/crear.html')
    #return redirect(reverse('persona: borrar', kwargs = {'pk':pk}))
    #return index_persona(request)
    #return redirect(reverse('persona:crear', kwargs='pk':pk))
    return redirect('persona:crear')

    
