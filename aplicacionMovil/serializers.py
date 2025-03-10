from rest_framework import serializers
from .models import *
#from .forms import *

class AplicacionMovilSerializer(serializers.ModelSerializer):
    fechaCreacion= serializers.DateField(format='%d-%m-%Y')
    
    class Meta:
        fields = ('nombre', 'fechaCreacion')
        model = AplicacionMovil
        
        
