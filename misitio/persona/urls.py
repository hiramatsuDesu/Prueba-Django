from django.urls import path
from persona.views import *

app_name = 'persona'

urlpatterns = [
    path('', index_persona),
    path('crear', crearUsuario, name='crear'),
    path('borrar/<int:pk>', borrarUsuario, name='borrar'),
    #path('lista', lista_usuarios)
]