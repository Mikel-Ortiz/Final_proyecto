import django
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, Contacto_formulario
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def Inicio(request):
    return render (request, 'Base/inicio.html')

def contacto(request):
    if request.method == 'POST':
        mi_formulario = Contacto_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion=mi_formulario.cleaned_data
            contacto = Contacto (nombre=informacion['nombre'],  correo=informacion['correo'], asunto=informacion['asunto'], mensaje=informacion['mensaje'])
            contacto.save()
            return render(request, 'Base/contacto.html', {'mensaje':"Mensaje enviado correctamente"})
    else:
        mi_formulario = Contacto_formulario()
    return render(request, 'Base/contacto.html', {'formulario':mi_formulario})

class Directorio_Lista(ListView):
    model = Laboratorio
    template_name = "Base/laboratorio_list.html"

class Directorio_Detalle(DetailView):
    model = Laboratorio
    template_name = "Base/laboratorio_detalle.html"

class Directorio_Creacion(LoginRequiredMixin, CreateView):
    model = Laboratorio
    success_url = reverse_lazy('laboratorio_listar')
    fields = ['nombre', 'descripción', 'foto']

class Directorio_Edicion(LoginRequiredMixin, UpdateView):
    model = Laboratorio
    success_url = reverse_lazy('laboratorio_listar')
    fields = ['nombre', 'descripción', 'foto']

class Directorio_Eliminacion(LoginRequiredMixin, DeleteView):
    model = Laboratorio
    success_url = reverse_lazy('laboratorio_listar')

#----------------------------------------------------------#

class Investigación_Lista(ListView):
    model = Linea_de_Investigacion
    template_name = "Base/investigación_list.html"

class Investigación_Detalle(DetailView):
    model = Linea_de_Investigacion
    template_name = "Base/investigación_detalle.html"

class Investigación_Creacion(LoginRequiredMixin, CreateView):
    model = Linea_de_Investigacion
    success_url = reverse_lazy('investigación_listar')
    fields = ['linea_de_investigacion', 'descripción', 'responsable']

class Investigación_Edicion(LoginRequiredMixin, UpdateView):
    model = Linea_de_Investigacion
    success_url = reverse_lazy('investigación_listar')
    fields = ['linea_de_investigacion', 'descripción', 'responsable']

class Investigación_Eliminacion(LoginRequiredMixin, DeleteView):
    model = Linea_de_Investigacion
    success_url = reverse_lazy('investigación_listar')

#----------------------------------------------------------#

class Evento_Lista(ListView):
    model = Eventos
    template_name = "Base/evento_list.html"

class Evento_Detalle(DetailView):
    model = Eventos
    template_name = "Base/evento_detalle.html"

class Evento_Creacion(LoginRequiredMixin, CreateView):
    model = Eventos
    success_url = reverse_lazy('evento_listar')
    fields = ['nombre', 'descripción', 'fecha']

class Evento_Edicion(LoginRequiredMixin, UpdateView):
    model = Eventos
    success_url = reverse_lazy('evento_listar')
    fields = ['nombre', 'descripción', 'fecha']

class Evento_Eliminacion(LoginRequiredMixin, DeleteView):
    model = Eventos
    success_url = reverse_lazy('evento_listar')

#----------------------------------------------------------#

class Blog_Lista(ListView):
    model = Blog
    template_name = "Base/blog_list.html"

class Blog_Detalle(DetailView):
    model = Blog
    template_name = "Base/blog_detalle.html"

class Blog_Creacion(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('blog_listar')
    fields = ['titulo', 'contenido', 'imagen','fecha_subido']

class Blog_Edicion(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('blog_listar')
    fields = ['titulo', 'contenido', 'imagen','fecha_subido']

class Blog_Eliminacion(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_listar')

#----------------------------------------------------------#

#----- LOGIN -----
def login_request(request):

    if request.method == 'POST':
        formulario2 = AuthenticationForm(request=request, data=request.POST)

        if formulario2.is_valid():
            usuario = formulario2.cleaned_data.get('username')
            contraseña = formulario2.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(request,'Base/inicio.html', {'usuario':usuario, 'mensaje':"Bienvenido al SEPIBLOG"})
            else:

                return render(request,'Base/login.html', {"mensaje":"Usuario incorrecto. Vuelva a intentar", 'formulario2':formulario2})
        else:
            return render(request,'Base/login.html', {"mensaje":"Formulario invalido. Vuelva a intentar", "formulario2":formulario2})
    else:
        formulario2 = AuthenticationForm()
        return render(request, 'Base/login.html', {'formulario2':formulario2})


def register(request):

    if request.method == 'POST':
        
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            formulario.save()
            return render(request, 'Base/login.html', {'usuario':usuario, 'mensaje':'Usuario creado correctamente. Ahora puede iniciar sesión'})
        else:
            return render(request, 'Base/register.html', {'mensaje':'No se pudo crear el usuario', 'formulario':formulario})
    else:
        formulario = UserRegistrationForm()
        return render(request, 'Base/register.html', {'formulario':formulario})