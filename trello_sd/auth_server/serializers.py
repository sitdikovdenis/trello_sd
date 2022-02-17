from rest_framework import serializers

from auth_server.models import Employee, SubDivision


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class SubDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDivision
        fields = '__all__'
