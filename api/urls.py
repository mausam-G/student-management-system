from django.urls import path

from .views import (StudentView, StudentDetailView, 
    StudentResultView, StudentResultDetailView,index
    )

urlpatterns = [
   path('', index, name='index'),
    path('student/', StudentView.as_view(), name='student_list_create'),
    path('student/<pk>', StudentDetailView.as_view(), name='student_retrieve_update_destroy'),
    path('student-result/', StudentResultView.as_view(), name='student_result_list_create'),
    path('student-result/<pk>', StudentResultDetailView.as_view(), name='student_result_retrieve_update_destroy'),
]