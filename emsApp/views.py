from email.policy import HTTP
from msilib.schema import ServiceInstall
from django.http import HttpResponse
from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from emsApp.serializers  import EmployeeSerializer
from django.http import Http404
from rest_framework import status

class EmployeeList(APIView):
    def get(self,request,format=None):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    

    def post(self,request,format=None):
        serializer=EmployeeSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)

class EmployeeDetails(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeByYear(APIView):
    def get(self,request,desgn,format=None):
        print(desgn)
        employees=Employee.objects.filter(designation__icontains=desgn)
        print (employees)
        serializer=EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


   

   