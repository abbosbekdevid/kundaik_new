# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated
from .models import SchoolModel,ClassModel
from .serializer import SchoolSerializer,ClassSerializer
from .permissions import IsOwnerGetbyUser

# Create your views here.
class ListCreateSchoolView(generics.ListCreateAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteSchoolView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = (IsOwnerGetbyUser,)

class ListCreateClassView(generics.ListCreateAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailUpdateDeleteClassView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer
    # permission_classes = (IsOwnerGetbyUser,)
