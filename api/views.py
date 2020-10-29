from django.shortcuts import render
from api.models import Todo
from django.http import JsonResponse
from api.serializers import TodoSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import permissions, authentication
from rest_framework.decorators import permission_classes, authentication_classes
from django.contrib.auth import login, logout, authenticate

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
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username', None)
            password = serializer.validated_data.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': "You're logged in."})
            else:
                return Response({'error': "Correct credentials were not provided"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': "Provide username and password."}, status=status.HTTP_400_BAD_REQUEST)

        
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': "You're logout"})

  