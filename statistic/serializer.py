from rest_framework import serializers
from .models import SubjectModel,AttendanceModel,GradeModel

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModel
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeModel
        fields = '__all__'
