from django.urls import path
from .api_views import *

urlpatterns = [
    path('listas-aplicacion/',aplicacionMovil_list, name="AplicacionMovil_list"),
    
    path(
        "aplicacion-eliminar/<int:aplicacion_id>/",
        aplicacion_eliminar,
        name="aplicacion_eliminar",
    ), 
    
    path('listas-comentarios/',comentarios_list, name="comentarios_list"),
    
    path(
        "comentario-eliminar/<int:comentario_id>/",
        comentario_eliminar,
        name="comentario_eliminar",
    ), 
    
    path('comentario/crear/',comentario_create),
    
    path('listar-usuarios/',usuarios_list), 
    
    path("comentario-nombre-editar/<int:comentario_id>/", comentario_editar_patch),
    
    path("texto-comentario/<int:comentario_id>/", obtener_comentario),
    #uRaq65UrNk4dAL5tVY32ghrBvnfJzI
     
    
    
    #sesiones
    #path('registrar/usuario',registrar_usuario.as_view()),
    
    
]