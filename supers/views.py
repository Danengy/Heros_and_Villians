from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Supers
from .serializers import SupersSerializer
from super_types.models import Super_Types
from super_types.serializers import Super_TypesSerializer

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = SupersSerializer(supers, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SupersSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, data=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def heroes_and_villians(request):
    
    super_type_param = request.query_params.get('type')
    queryset = Supers.objects.all()
    if super_type_param:
        queryset = queryset.filter(type__type=super_type_param)
    
        serializer = SupersSerializer(queryset, many = True)
        return SupersSerializer(serializer.data)


    # hero = Super_Types.objects.filter(type = 'Hero')
    # villian = Super_Types.objects.filter(type='Villian')
    # serializer = Super_TypesSerializer(super_types, many=True)

    # custom_response = {
    #     'Hero': serializer.data,
    #     'Villians': serializer.data
    # }

