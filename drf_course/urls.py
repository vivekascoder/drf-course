from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import urls
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('t', views.TodoViewSet)
router.register('teachers', views.TeacherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/<int:pk>', views.TodoView.as_view(), name='todo'),
    path('todo', views.TodoListView.as_view(), name='todo-create'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('c_t', views.TeacherView.as_view()),
]

urlpatterns += router.urls
