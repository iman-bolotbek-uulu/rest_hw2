import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework import viewsets

from . import models
from . import serializers

from datetime import datetime, date


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
#Это для функции create_employee GET запроса,дату не показывала


@csrf_exempt
def create_position(request):
    if request.method == 'GET':
        positions = models.Position.objects.all()
        info = []
        for position in positions:
            info.append({'positions': position.positions, 'departments': position.departments})
        json_data = json.dumps(info)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        info = json.loads(request.body)
        new_position = models.Position.objects.create(**info)
        json_data = {'positions': new_position.positions, 'departments': new_position.departments}
        return JsonResponse(json_data, safe=False)


class PositionViewSet(viewsets.ModelViewSet):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer



@csrf_exempt
def create_employee(request):
    if request.method == 'GET':
        employees = models.Employee.objects.all()
        info = []
        for employee in employees:
            info.append({'fullname': employee.fullname, 'date_birth': employee.date_birth,'salary': employee.salary, 'position': employee.position.id})
        json_data = json.dumps(info, default=json_serial)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        info = json.loads(request.body)
        new_employee = models.Employee.objects.create(**info)
        json_data = {'fullname': new_employee.fullname, 'date_birth': new_employee.date_birth,'salary': new_employee.salary, 'position': new_employee.position.id}
        return JsonResponse(json_data, safe=False)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer