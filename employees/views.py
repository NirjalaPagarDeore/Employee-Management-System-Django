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


######  Delete Employee
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect("employee_list")

######  Update Employee
def update_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.employee_id = request.POST["employee_id"]
        employee.name = request.POST["name"]
        employee.email = request.POST["email"]
        employee.phone = request.POST["phone"]
        employee.gender = request.POST["gender"]
        employee.date_of_birth = request.POST["date_of_birth"]
        employee.department = request.POST["department"]
        employee.designation = request.POST["designation"]
        employee.joining_date = request.POST["joining_date"]
        employee.employment_type = request.POST["employment_type"]
        employee.salary = request.POST["salary"]
        employee.experience = request.POST["experience"]
        employee.manager = request.POST["manager"]
        employee.address = request.POST["address"]
        employee.city = request.POST["city"]
        employee.state = request.POST["state"]
        employee.pincode = request.POST["pincode"]
        employee.status = request.POST["status"]
        employee.emergency_contact = request.POST["emergency_contact"]
        employee.message = request.POST.get("message", "")

        employee.save()

        return redirect("employee_list")

    return render(
        request,
        "employees/update_employee.html",
        {"employee": employee}
    )

#####View employee details
def view_employee(request, id):

    employee = Employee.objects.get(id=id)

    return render(
        request,
        "employees/view_employee.html",
        {"employee": employee}
    )