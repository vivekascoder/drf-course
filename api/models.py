from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    SECTION = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    division = models.PositiveIntegerField(default=0)
    section = models.CharField(choices=SECTION, max_length=1)
    image = models.ImageField(upload_to="StudentImages")

    def my_section(self):
        return self.section
    
    class Meta:
        ordering = ('-division',)

class Todo(models.Model):
    task = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-time',)


class Person(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return self.name
