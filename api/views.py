from django.shortcuts import render
from api.models import Todo
from django.http import JsonResponse
from api.serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class TodoView(APIView):
    def get_queryset(self, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {
                    "error": f"There is no todo having primary key {pk}"
                }
            )
        return todo
    
    def get(self, request, pk):
        todo = self.get_queryset(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = self.get_queryset(pk)
        print(request.data)
        serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = self.get_queryset(pk)
        serializer = TodoSerializer(instance=todo)
        todo.delete()
        return Response(serializer.data)


class TodoListView(APIView):
    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




    