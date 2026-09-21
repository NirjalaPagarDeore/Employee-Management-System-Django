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
    path("search_employee/", views.search_employee, name="search_employee"),

    ##Department paths
     path("add_department/", views.add_department, name="add_department"),
       path("department_list/", views.department_list, name="department_list"),

     path("delete_department/<int:id>/", views.delete_department, name="delete_department"),
     path("update_department/<int:id>/", views.update_department, name="update_department"),

      path("add_leave/", views.add_leave, name="add_leave"),
      path("leave_list/", views.leave_list, name="leave_list"),

      path("approve-leave/<int:id>/", views.approve_leave,name="approve_leave"),
      path(
        "attendance/add/",
        views.attendance_add,
        name="attendance_add"
    ),

    path(
        "attendance/",
        views.attendance_list,
        name="attendance_list"
    ),

]
