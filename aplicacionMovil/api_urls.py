from django.urls import path
from .api_views import *

urlpatterns = [
    path('listas-aplicacion/',AplicacionMovil_list, name="AplicacionMovil_list"),
    
]