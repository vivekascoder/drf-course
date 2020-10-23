from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    SECTION = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    division = models.PositiveIntegerField(default=0)
    section = models.CharField(choices=SECTION, max_length=1)

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