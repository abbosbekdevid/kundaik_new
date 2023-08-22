# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated
from .models import SubjectModel,AttendanceModel,GradeModel
from .serializer import SubjectSerializer,AttendanceSerializer,GradeSerializer
from .permissions import IsOwnerGetbyUser

# Create your views here.
class ListCreateSubjectView(generics.ListCreateAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteSubjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = (IsOwnerGetbyUser,)

class ListCreateAttendanceView(generics.ListCreateAPIView):
    queryset = AttendanceModel.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteAttendanceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceModel.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = (IsOwnerGetbyUser,)

class ListCreateGradeView(generics.ListCreateAPIView):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteGradeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializer
    # permission_classes = (IsOwnerGetbyUser,)
