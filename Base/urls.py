from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Inicio, name='inicio'),
    
    path('directorio/list/', Directorio_Lista.as_view(), name='laboratorio_listar'),
    path('directorio/<pk>', Directorio_Detalle.as_view(), name='laboratorio_detalle'),
    path('directorio/nuevo/', Directorio_Creacion.as_view(), name='laboratorio_crear'),
    path('directorio/editar/<pk>', Directorio_Edicion.as_view(), name='laboratorio_editar'),
    path('directorio/borrar/<pk>', Directorio_Eliminacion.as_view(), name='laboratorio_borrar'),

    path('linea/list/', Investigación_Lista.as_view(), name='investigación_listar'),
    path('linea/<pk>', Investigación_Detalle.as_view(), name='investigación_detalle'),
    path('linea/nuevo/', Investigación_Creacion.as_view(), name='investigación_crear'),
    path('linea/editar/<pk>', Investigación_Edicion.as_view(), name='investigación_editar'),
    path('linea/borrar/<pk>', Investigación_Eliminacion.as_view(), name='investigación_borrar'),

    path('evento/list/', Evento_Lista.as_view(), name='evento_listar'),
    path('evento/<pk>', Evento_Detalle.as_view(), name='evento_detalle'),
    path('evento/nuevo/', Evento_Creacion.as_view(), name='evento_crear'),
    path('evento/editar/<pk>', Evento_Edicion.as_view(), name='evento_editar'),
    path('evento/borrar/<pk>', Evento_Eliminacion.as_view(), name='evento_borrar'),

    path('blog/list/', Blog_Lista.as_view(), name='blog_listar'),
    path('blog/<pk>', Blog_Detalle.as_view(), name='blog_detalle'),
    path('blog/nuevo/', Blog_Creacion.as_view(), name='blog_crear'),
    path('blog/editar/<pk>', Blog_Edicion.as_view(), name='blog_editar'),
    path('blog/borrar/<pk>', Blog_Eliminacion.as_view(), name='blog_borrar'),

    path('contacto/', contacto, name='contacto'),

    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='Base/logout.html'), name='logout'),
]