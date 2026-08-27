from django.shortcuts import render,redirect
from .models  import Employee

# Create your views here.
def dashboard(request):
    return render(request, "employees/dashboard.html")

def forms(request):
    return render(request, "employees/forms.html")

def add_employee(request):

    if request.method == "POST":

        Employee.objects.create(
            employee_id=request.POST["employee_id"],
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            gender=request.POST["gender"],
            date_of_birth=request.POST["date_of_birth"],
            department=request.POST["department"],
            designation=request.POST["designation"],
            joining_date=request.POST["joining_date"],
            employment_type=request.POST["employment_type"],
            salary=request.POST["salary"],
            experience=request.POST["experience"],
            manager=request.POST["manager"],
            address=request.POST["address"],
            city=request.POST["city"],
            state=request.POST["state"],
            pincode=request.POST["pincode"],
            status=request.POST["status"],
            emergency_contact=request.POST["emergency_contact"],
            message=request.POST.get("message", "")
        )

        return redirect("employee_list")

    return render(request, "employees/add_employee.html")

def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        "employees/employee_list.html",
        {"employees": employees}
    )