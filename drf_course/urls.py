from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/<int:pk>', views.todo, name='todo'),
    path('todo', views.create_todo, name='todo-create'),
]
