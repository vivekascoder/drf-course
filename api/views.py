from django.shortcuts import render
from api.models import Todo
from django.http import JsonResponse
from api.serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
def todo(request, pk):
    def get_queryset():
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {
                    "error": f"There is no todo having primary key {pk}"
                }
            )
        return todo
    
    if request.method == "GET":
        todo = get_queryset()
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        todo = get_queryset()
        print(request.data)
        serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        todo = get_queryset()
        todo.delete()
        return Response({'msg': "Deleted"})


@api_view(['GET', 'POST'])
def create_todo(request):
    if request.method == "GET":
        queryset = Todo.objects.all()
        serializer = TodoSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)

    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




    