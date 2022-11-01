from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Supers
from .serializers import SupersSerializer


@api_view(['GET', 'POST'])
def heroes_villians(request):

    if request.method == 'GET':
        heroes = Supers.objects.filter(super_type__type='Hero')
        villians = Supers.objects.filter(super_type__type='Villian')
        heroes_serializer = SupersSerializer(heroes, many=True)
        villian_serializer = SupersSerializer(villians, many=True)
        super_type_param = request.query_params.get('super_type')
        print(super_type_param)
        supers = Supers.objects.all()
        if super_type_param:
            supers =supers.filter(super_type__type=super_type_param)
        elif not super_type_param:
            custom_reponse = {
            'Hero' : heroes_serializer.data,
            'Villian': villian_serializer.data
        }
            return Response(custom_reponse)
        serializer = SupersSerializer(supers, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SupersSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
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



    