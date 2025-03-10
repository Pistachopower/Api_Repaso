from rest_framework import serializers
from .models import *
#from .forms import *

class AplicacionMovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = AplicacionMovil
        fields = '__all__'
        
