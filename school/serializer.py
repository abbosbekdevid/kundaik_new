from rest_framework import serializers
from .models import SchoolModel,ClassModel

class SchoolSerializer(serializers.ModelSerializer):
    model = SchoolModel
    fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = '__all__'