from dataclasses import fields
from pyexpat import model
from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['emp_id','emp_name','designation','join_date']
        