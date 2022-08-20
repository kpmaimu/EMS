from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=200)
    designation=models.CharField(max_length=100)
    join_date=models.DateField(blank=True,default='2020-03-13')
    def __str__(self):
        return self.emp_name

