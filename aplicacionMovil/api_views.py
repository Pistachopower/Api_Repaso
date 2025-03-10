from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AplicacionMovil
from .serializers import *

@api_view(['GET'])
def AplicacionMovil_list(request):
    consultaAplicacionmovil = AplicacionMovil.objects.all()
    serializer= AplicacionMovilSerializer(consultaAplicacionmovil, many=True)
    return Response(serializer.data)
    