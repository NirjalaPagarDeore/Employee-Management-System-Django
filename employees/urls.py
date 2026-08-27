from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
     path("forms/", views.forms, name="forms"),
     path("add_employee/", views.add_employee, name="add_employee"),
      
    path("employee_list/", views.employee_list, name="employee_list"),

]
