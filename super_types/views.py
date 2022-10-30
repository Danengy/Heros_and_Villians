from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super_Types 
from .serializers import Super_TypesSerializer

@api_view(['GET'])
def super_types_list(request):
    type = Super_Types.objects.all()
    serializer = Super_TypesSerializer(type, many = True)
    return Response(serializer.data)
