from rest_framework import serializers

from apiapp.models import student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('id', 'firstname', 'lastname')