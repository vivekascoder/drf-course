from django.shortcuts import render
from api.models import Todo
from django.http import JsonResponse
from api.serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

# !Create your views here.


# !RUD Operations using mixins
# class TodoView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class TodoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

# ? LC Operations  using rest_framework mixins.
# class TodoListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    