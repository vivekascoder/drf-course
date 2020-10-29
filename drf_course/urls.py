from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/<int:pk>', views.TodoView.as_view(), name='todo'),
    path('todo', views.TodoListView.as_view(), name='todo-create'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
