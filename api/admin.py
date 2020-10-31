from django.contrib import admin
from api.models import Todo, Student, Teacher

# Register your models here.
admin.site.register((Todo, Student, Teacher))