import json

from rest_framework import serializers

from . import models

from django.http import JsonResponse


class PositionSerializer(serializers.Serializer):
    positions = serializers.CharField(max_length=30)
    departments = serializers.CharField(max_length=30)

    def create(self, validated_data):
        data = json.load(validated_data)
        new_position = models.Position.objects.create(**data)
        json_data = {'positions': new_position.positions, 'departments': new_position.departments}
        return JsonResponse(json_data, safe=False)

    def update(self, instance, validated_data):
        data = json.load(instance)
        json_data = {'positions': data.positions, 'departments': data.departments}
        return JsonResponse(json_data, safe=False)


class EmployeeSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=30)
    date_birth = serializers.DateField()
    salary = serializers.DateField()
    position = serializers.IntegerField()

    def create(self, validated_data):
        data = json.load(validated_data)
        new_employee = models.Employee.objects.create(**data)
        json_data = {'fullname': new_employee.fullname, 'date_birth': new_employee.date_birth, 'salary': new_employee.salary, 'position': new_employee.position.id}
        return JsonResponse(json_data, safe=False)

    def update(self, instance, validated_data):
        data = json.load(instance)
        json_data = {'fullname': data.fullname, 'date_birth': data.date_birth, 'salary': data.salary, 'position': data.position.id}
        return JsonResponse(json_data, safe=False)