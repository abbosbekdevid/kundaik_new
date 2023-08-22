from rest_framework import serializers
from .models import StudentModel,TeacherModel,ParentsModel

class ParentsSerializer(serializers.ModelSerializer):
    model = ParentsModel
    fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'