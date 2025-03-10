from django.shortcuts import render

from aplicacionMovil.models import AplicacionMovil

# Create your views here.
def index(request):
   return render(request, 'index.html')


def AplicacionMovil_list(request):
   aplicacion= AplicacionMovil.objects.all()
   return render(request, 'listar.html', {'aplicacion': aplicacion})
    
