from django.urls import path
from account.views import (ListCreateStudentView,DetailUpdateDeleteStudentView,
                           ListCreateTeacherView,DetailUpdateDeleteTeacherView,
                           ListCreateParentsView,DetailUpdateDeleteParentsView,)

urlpatterns = [
    path('student/',ListCreateStudentView.as_view()),
    path('student/<pk>/',DetailUpdateDeleteStudentView.as_view()),
    path('teacher/',ListCreateTeacherView.as_view()),
    path('teacher/<pk>/',DetailUpdateDeleteTeacherView.as_view()),
    path('parent/',ListCreateParentsView.as_view()),
    path('parent/<pk>/',DetailUpdateDeleteParentsView.as_view()),
]