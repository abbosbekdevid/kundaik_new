from django.urls import path
from statistic.views import (ListCreateSubjectView,DetailUpdateDeleteSubjectView,
                             ListCreateAttendanceView,DetailUpdateDeleteAttendanceView,
                             ListCreateGradeView,DetailUpdateDeleteGradeView,)

urlpatterns = [
    path('subject/',ListCreateSubjectView.as_view()),
    path('subject/<pk>/',DetailUpdateDeleteSubjectView.as_view()),
    path('attendance/',ListCreateAttendanceView.as_view()),
    path('attendance/<pk>/',DetailUpdateDeleteAttendanceView.as_view()),
    path('grade/',ListCreateGradeView.as_view()),
    path('grade/<pk>/',DetailUpdateDeleteGradeView.as_view()),
]