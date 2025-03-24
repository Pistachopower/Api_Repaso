from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AplicacionMovil
from rest_framework import status
from .serializers import *


@api_view(["GET"])
def aplicacionMovil_list(request):
    consultaAplicacionmovil = AplicacionMovil.objects.all()
    serializer = AplicacionMovilSerializer(consultaAplicacionmovil, many=True)
    return Response(serializer.data)

#usuarios_list
@api_view(["GET"])
def usuarios_list(request):
    consultaUsuario = Usuario.objects.all()
    serializer = UsuarioSerializer(consultaUsuario, many=True)
    return Response(serializer.data)



# aplicacion_eliminar
# pedido_eliminar
@api_view(["DELETE"])
def aplicacion_eliminar(request, aplicacion_id):

    aplicacion = AplicacionMovil.objects.get(id=aplicacion_id)
    try:
        aplicacion.delete()
        return Response("aplicacion ELIMINADO")
    except Exception as error:
        return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def comentarios_list(request):
    # hacemos la consulta que trae todos los registros
    consulta_comentarios = Comentario.objects.select_related(
        "aplicacion_movil", "usuario"
    ).all()

    # serializamos, es decir, lo pasamos a un formato valido
    serializer = ComentariosSerializer(consulta_comentarios, many=True)

    # lo enviamos
    return Response(serializer.data)


@api_view(["DELETE"])
def comentario_eliminar(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    try:
        comentario.delete()
        
        return Response("comentario ELIMINADO")
    except Exception as error:
        return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def comentario_create(request):
    print(request.data)
    comentarioCreateSerializer = ComentariosSerializerCreate(data=request.data)

    if comentarioCreateSerializer.is_valid():
        try:
            comentarioCreateSerializer.save()
            print("Datos validados:", comentarioCreateSerializer.validated_data)
            return Response("comentario CREADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(repr(error))
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(
            comentarioCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["PATCH"])
def comentario_editar_patch(request, comentario_id):
        
    comentario = Comentario.objects.get(id=comentario_id)
    
    comentarioSerializer = ComentariosSerializer(
        comentario, data=request.data, partial=True
    )
    if comentarioSerializer.is_valid():
        try:
            comentarioSerializer.save()
            return Response("Nombre de comentario EDITADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(
            comentarioSerializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET"])
def obtener_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    
    serializer = ComentariosSerializer(comentario)
    
    
    return Response(serializer.data)  


#comentario_editar_put

@api_view(['PUT'])
def comentario_editar_put(request,comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    
    comentarioCreateSerializer = ComentariosSerializerCreate(data=request.data,instance=comentario)
    
    if comentarioCreateSerializer.is_valid():
        try:
            comentarioCreateSerializer.save()
            return Response("Comentario EDITADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(comentarioCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# SESIONES
# from rest_framework import generics
# from rest_framework.permissions import AllowAny
# class registrar_usuario(generics.CreateAPIView):
#    serializer_class = UsuarioSerializerRegistro
#    permission_classes = [AllowAny]
#
#    def create(self, request, *args, **kwargs):
#        serializers = UsuarioSerializerRegistro(data=request.data)
#        if serializers.is_valid():
#            try:
#                rol = request.data.get('rol')
#                #creacion del usuario
#                user = Usuario.objects.create_user(
#                        nombre= serializers.data.get("nombre"),
#                        last_name= serializers.data.get("last_name"),
#                        telefono= serializers.data.get("telefono"),
#                        username = serializers.data.get("username"),
#                        correo = serializers.data.get("correo"),
#                        password = serializers.data.get("password1"),
#                        rol = rol,
#                        )
#
#                #Creación de perfil según rol:
#                if(rol == Usuario.CLIENTE):
#                    cliente = Cliente.objects.create( usuario = user)
#                    cliente.save()
#                elif(rol == Usuario.EMPLEADO):
#                    empleado = Empleado.objects.create(usuario = user)
#                    empleado.save()
#                usuarioSerializado = UsuarioSerializer(user)
#                return Response(usuarioSerializado.data)
#            except Exception as error:
#                print(repr(error))
#                return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#        else:
#            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
