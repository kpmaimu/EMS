from django.urls import path
# from EMS.emsApp.views import EmployeeByYear
from emsApp import views

urlpatterns=[

    path('list/', views.EmployeeList.as_view()),
    path('details/<int:pk>',views.EmployeeDetails.as_view()),
    path('list/designation/<str:desgn>', views.EmployeeByYear.as_view()),
]

