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
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

# !Create your views here.



class TodoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()



class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [ authentication.TokenAuthentication]


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username', None)
            password = serializer.validated_data.get('password', None)
        # if len(password) > 7:
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    t = Token.objects.get(user=user)
                except Token.DoesNotExist:
                    t = Token.objects.create(user=user)
                auth_token = t.key
                return Response({'message': "You're logged in.", 'token': auth_token})
            else:
                return Response({'error': "Correct credentials were not provided"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': "Provide username and password."}, status=status.HTTP_400_BAD_REQUEST)

        
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': "You're logout"})

  



class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=['GET'])
    def data(self, request, **kwargs):
        return Response({'message': 'Nested Route'})