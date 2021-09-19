from django.shortcuts import render

from rest_framework import generics

from rest_framework.response import Response


from .models import CustomUser, Teacher, Student, StudentResult
from .serializers import CustomUserSerializer, TeacherSerializer, StudentSerializer, StudentResultSerializer

class CustomUserView(generics.ListCreateAPIView):
    model = CustomUser
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class TeacherView(generics.ListCreateAPIView):
    model = Teacher
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentView(generics.ListCreateAPIView):
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentResultView(generics.ListCreateAPIView):
    model = StudentResult
    queryset = StudentResult.objects.all()
    serializer_class = StudentResultSerializer

class StudentResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = StudentResult
    queryset = StudentResult.objects.all()
    serializer_class = StudentResultSerializer