from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated
from .models import StudentModel,TeacherModel,ParentsModel
from .serializer import StudentSerializer,TeacherSerializer,ParentsSerializer
from .permissions import IsOwnerGetbyUser

# Create your views here.
class ListCreateStudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (IsOwnerGetbyUser,)

class ListCreateTeacherView(generics.ListCreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteTeacherView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = (IsOwnerGetbyUser,)

class ListCreateParentsView(generics.ListCreateAPIView):
    queryset = ParentsModel.objects.all()
    serializer_class = ParentsSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteParentsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = ParentsSerializer
    # permission_classes = (IsOwnerGetbyUser,)
