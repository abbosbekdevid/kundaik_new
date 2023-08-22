from django.urls import path
from school.views import (ListCreateSchoolView,DetailUpdateDeleteSchoolView,
                          ListCreateClassView,DetailUpdateDeleteClassView,)

urlpatterns = [
    path('school/',ListCreateSchoolView.as_view()),
    path('school/<pk>/',DetailUpdateDeleteSchoolView.as_view()),
    path('class/',ListCreateClassView.as_view()),
    path('class/<pk>/',DetailUpdateDeleteClassView.as_view()),
]