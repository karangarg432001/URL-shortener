from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apiapp.models import student
from apiapp.serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer