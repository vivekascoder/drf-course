from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import urls
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
# router = DefaultRouter()
router.register('t', views.TodoViewSet)
router.register('teachers', views.TeacherViewSet)
router.register('students', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/<int:pk>', views.TodoView.as_view(), name='todo'),
    path('todo', views.TodoListView.as_view(), name='todo-create'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('c_t', views.TeacherView.as_view()),
]

urlpatterns += router.urls
urlpatterns += format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)