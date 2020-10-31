from rest_framework import serializers
import datetime
from api.models import Todo, Teacher, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ['task', 'is_completed', 'time']
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields ='__all__'
        depth = 1
    
    def create(self, validated_data):
        teacher = Teacher.objects.create(name=validated_data.get('name', None))
        students = validated_data.get('students', None)
        if students:
            for student in students:
                print(student)
        return self
        
