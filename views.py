from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Soda
from soda_app.serializer import SodaSerializer
from rest_framework import status
 
 

# Create your views here.
@api_view(['GET', 'post'])
def soda_list(request,format=None):
    if request.method =='GET':
        all_soda = Soda.objects.all()
        serializer = SodaSerializer(all_soda, many=True)
        return Response(serializer.data)
   

    if request.method == 'POST':
       serializer = SodaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def soda_detail(request,id ,format=None):
    try:
     Sodas=Soda.objects.get(pk=id)
    except Soda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        serializer = SodaSerializer(Sodas)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer= SodaSerializer(Sodas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    elif request.method == 'DELETE':
        Sodas.delete()
        return Response(status=status.HTTP_200_OK)
