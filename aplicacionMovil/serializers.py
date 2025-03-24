from datetime import date
from rest_framework import serializers
from .models import *
#from .forms import *

class AplicacionMovilSerializer(serializers.ModelSerializer):
    fechaCreacion= serializers.DateField(format='%d-%m-%Y')
    
    class Meta:
        fields = ('nombre', 'fechaCreacion', 'id')
        model = AplicacionMovil
        
class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'username')
        model = Usuario

        
        
        

class ComentariosSerializer(serializers.ModelSerializer):
     #Recuerda que los atributos relacionados deben coicidir con el tipo de dato de los modelos
    aplicacion_movil_nombre = serializers.CharField(source='aplicacion_movil.nombre', read_only=True)
    usuario_rol = serializers.IntegerField(source='usuario.rol', read_only=True)

    class Meta:
        model = Comentario
        fields = ['texto_comentario', 'aplicacion_movil_nombre', 'puntuacion', 'usuario_rol', 'fecha_comentario', 'id']
     
    #importante: el nombre de la funcion debe ser validate_<nombre del campo> para que funcione  
    def validate_texto_comentario(self, texto_comentario_param):
        consulta_comentario = Comentario.objects.filter(texto_comentario=texto_comentario_param).first()
        if not consulta_comentario is None:  # sino es nulo
            if consulta_comentario.texto_comentario == texto_comentario_param:
                    raise serializers.ValidationError("No puedes colocar comentario repetido")
        return texto_comentario_param
        

class ComentariosSerializerCreate(serializers.ModelSerializer):
    
    class Meta:
        model = Comentario
        fields = ['texto_comentario', 'aplicacion_movil', 'puntuacion', 'usuario', 'fecha_comentario']
        
        
        
    def validate_texto_comentario(self, texto_comentario_param):
        consulta_comentario = Comentario.objects.filter(texto_comentario=texto_comentario_param).first()
        if not consulta_comentario is None:  # sino es nulo
            if consulta_comentario.texto_comentario == texto_comentario_param:
                    raise serializers.ValidationError("El comentario ya existe")
        return texto_comentario_param


    def validate_fecha_comentario(self, fecha_comentario):
        fecha_hoy = date.today()

        # Obtener la aplicación móvil relacionada con el comentario
        aplicacion_movil = self.initial_data.get("aplicacion_movil")
        

        aplicacion_bd = AplicacionMovil.objects.get(id=aplicacion_movil)

        if not aplicacion_bd:
            raise serializers.ValidationError("No se pudo obtener la aplicación móvil asociada al comentario.")

        # Obtener la fecha de creación de la aplicación móvil
        fecha_creacion_aplicacion = aplicacion_bd.fechaCreacion

        # Validaciones
        if fecha_comentario > fecha_hoy:
            raise serializers.ValidationError("La fecha del comentario no puede ser en el futuro.")

        if fecha_comentario < fecha_creacion_aplicacion:
            raise serializers.ValidationError("La fecha del comentario no puede ser anterior a la creación de la aplicación móvil.")

        return fecha_comentario

    # def validate_metodo_pago(self, metodo):
    #     metodobd = MetodoPago.objects.get(id=metodo.id)
    #     if metodobd is None:
    #         raise serializers.ValidationError("El metodo seleccionado no existe")
    #     return metodo
        
        
        



       
#class UsuarioSerializerRegistro(serializers.Serializer):
#    username = serializers.CharField()
#    password1 = serializers.CharField()
#    password2 = serializers.CharField()
#    correo = serializers.EmailField()
#    rol = serializers.IntegerField()
#    nombre = serializers.CharField()
#    last_name = serializers.CharField()
#    telefono = serializers.CharField()
#
#    def validate_username(self, username):
#        usuario = Usuario.objects.filter(username=username).first()
#        if not usuario is None:
#            raise serializers.ValidationError("Ya existe un usuario con ese nombre")
#        return username
        
        
