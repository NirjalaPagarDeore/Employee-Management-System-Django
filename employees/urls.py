from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
     path("forms/", views.forms, name="forms"),
     path("add_employee/", views.add_employee, name="add_employee"),
      
    path("employee_list/", views.employee_list, name="employee_list"),
    path("delete_employee/<int:id>/", views.delete_employee, name="delete_employee"),
    path("update_employee/<int:id>/", views.update_employee, name="update_employee"),

    path("view_employee/<int:id>/", views.view_employee, name="view_employee"),

]
