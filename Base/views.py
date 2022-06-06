import django
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, Contacto_formulario
from django.contrib.auth.views import LogoutView

# Create your views here.
def Inicio(request):
    return render (request, 'Base/inicio.html')

def contacto(request):
    contact_form= Contacto_formulario
    return(request, 'Base/contacto.html', {'formulario':contact_form})

class Directorio_Lista(ListView):
    model = Laboratorio
    template_name = "Base/laboratorio_list.html"

class Directorio_Detalle(DetailView):
    model = Laboratorio
    template_name = "Base/laboratorio_detalle.html"

class Directorio_Creacion(CreateView):
    model = Laboratorio
    success_url = reverse_lazy('laboratorio_listar')
    fields = ['nombre', 'descripción', 'foto']

class Directorio_Edicion(UpdateView):
    model = Laboratorio
    success_url = reverse_lazy('laboratorio_listar')
    fields = ['nombre', 'descripción', 'foto']

class Directorio_Eliminacion(DeleteView):
    model = Laboratorio
    success_url = reverse_lazy('laboratorio_listar')

#----------------------------------------------------------#

class Investigación_Lista(ListView):
    model = Linea_de_Investigacion
    template_name = "Base/investigación_list.html"

class Investigación_Detalle(DetailView):
    model = Linea_de_Investigacion
    template_name = "Base/investigación_detalle.html"

class Investigación_Creacion(CreateView):
    model = Linea_de_Investigacion
    success_url = reverse_lazy('investigación_listar')
    fields = ['linea_de_investigacion', 'descripción', 'responsable']

class Investigación_Edicion(UpdateView):
    model = Linea_de_Investigacion
    success_url = reverse_lazy('investigación_listar')
    fields = ['linea_de_investigacion', 'descripción', 'responsable']

class Investigación_Eliminacion(DeleteView):
    model = Linea_de_Investigacion
    success_url = reverse_lazy('investigación_listar')

#----------------------------------------------------------#

class Evento_Lista(ListView):
    model = Eventos
    template_name = "Base/evento_list.html"

class Evento_Detalle(DetailView):
    model = Eventos
    template_name = "Base/evento_detalle.html"

class Evento_Creacion(CreateView):
    model = Eventos
    success_url = reverse_lazy('evento_listar')
    fields = ['nombre', 'descripción', 'fecha']

class Evento_Edicion(UpdateView):
    model = Eventos
    success_url = reverse_lazy('evento_listar')
    fields = ['nombre', 'descripción', 'fecha']

class Evento_Eliminacion(DeleteView):
    model = Eventos
    success_url = reverse_lazy('evento_listar')

#----------------------------------------------------------#

class Blog_Lista(ListView):
    model = Entradas_blog
    template_name = "Base/blog_list.html"

class Blog_Detalle(DetailView):
    model = Entradas_blog
    template_name = "Base/blog_detalle.html"

class Blog_Creacion(CreateView):
    model = Entradas_blog
    success_url = reverse_lazy('blog_listar')
    fields = ['titulo', 'contenido', 'imagen','fecha_subido']

class Blog_Edicion(UpdateView):
    model = Entradas_blog
    success_url = reverse_lazy('blog_listar')
    fields = ['titulo', 'contenido', 'imagen','fecha_subido']

class Blog_Eliminacion(DeleteView):
    model = Entradas_blog
    success_url = reverse_lazy('blog_listar')

#----------------------------------------------------------#

#----- LOGIN -----
def login_request(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request=request, data=request.POST)

        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(request,'Base/inicio.html', {'usuario':usuario, 'mensaje':"Bienvenido a SEPIBLOG"})
            else:

                return render(request,'Base/login.html', {"mensaje":"Usuario incorrecto. Vuelva a intentar"})
        else:
            return render(request,'Base/login.html', {"mensaje":"Formulario invalido. Vuelva a intentar"})
    else:
        formulario = AuthenticationForm()
        return render(request, 'Base/login.html', {'formulario':formulario})


def register(request):

    if request.method == 'POST':
        
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get['username']
            formulario.save()
            return render(request, 'Base/login.html', {'usuario':usuario, 'mensaje':'Usuario creado correctamente'})
        else:
            return render(request, 'Base/register.html', {'mensaje':'No se pudo crear el usuario'})
    else:
        formulario = UserRegistrationForm()
        return render(request, 'Base/register.html', {'formulario':formulario})