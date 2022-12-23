from django.db import models


class Position(models.Model):
    positions = models.CharField(max_length=30)
    departments = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.position} - {self.department}'


class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    date_birth = models.DateField()
    salary = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employee')

    def __str__(self):
        return self.fullname


