from django.shortcuts import render,redirect
from .models  import Employee , Department
from .models import Department
from .models import Leave
from django.http import JsonResponse
from .models import Attendance
from .forms import AttendanceForm

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
            department_id=request.POST.get("department"),
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

    # Get departments for dropdown
    departments = Department.objects.all()

    return render(
        request,
        "employees/add_employee.html",
        {"departments": departments}
    )

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
        department_id=request.POST.get("department"),
        
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
    
    departments = Department.objects.all()
    return render(
        request,
        "employees/update_employee.html",
        {"employee": employee, "departments": departments}
    )

#####View employee details
def view_employee(request, id):

    employee = Employee.objects.get(id=id)

    return render(
        request,
        "employees/view_employee.html",
        {"employee": employee}
    )

######## Search  Employee
def search_employee(request):

    search = request.GET.get("search", "")

    employees = Employee.objects.filter(
        name__icontains=search
    )

    data = []

    for employee in employees:

        data.append({
            "id": employee.id,
            "employee_id": employee.employee_id,
            "name": employee.name,
            "phone": employee.phone,
            "email": employee.email,
            "employment_type": employee.employment_type,
            "department": employee.department,
            "designation": employee.designation,
            "manager": employee.manager,
        })

    return JsonResponse(data, safe=False)

####Department
def add_department(request):

    if request.method == "POST":

        department_id = request.POST.get("department_id")
        department_name = request.POST.get("department_name")
        description = request.POST.get("description")
        status = request.POST.get("status")

        Department.objects.create(
            department_id=department_id,
            department_name=department_name,
            description=description,
            status=status
        )

        return redirect('department_list')

    return render(request, 'employees/add_department.html')


def department_list(request):

       department = Department.objects.all()
       
       return render(
               request,
               "employees/department_list.html",
               {"departments": department}
           )


def delete_department(request, id):


   department = Department.objects.get(id=id)

   department.delete()
   return redirect("department_list")


####Update Department
def update_department(request, id):

    department = Department.objects.get(id=id)

    if request.method == "POST":

        department.department_id = request.POST["department_id"]
        department.department_name = request.POST["department_name"]
        department.description = request.POST["description"]
        department.status = request.POST["status"]
        

        department.save()

        return redirect("department_list")

    return render(
        request,
        "employees/update_department.html",
        {"department": department}
    )


def add_leave(request):

    employees = Employee.objects.all()

    if request.method == "POST":
    
           
            employee_id = request.POST.get("employee_id")
            reason = request.POST.get("reason")
            from_date = request.POST.get("from_date")
            to_date = request.POST.get("to_date")
            leave_type = request.POST.get("leave_type")

            
            Leave.objects.create(
              
                employee_id=employee_id,
                reason=reason,
                from_date = from_date,
                to_date = to_date,
                leave_type=leave_type
            )
    
            return redirect('leave_list')
    return render(request, 'employees/add_leave.html', {"employees": employees})


def leave_list(request):
   
       leaves  = Leave.objects.all()
       
       return render(
               request,
               "employees/Leave_list.html",
               {"leaves": leaves }
           )


##### Aprove leave
def approve_leave(request, id):

    # Find the leave record
    leave = Leave.objects.get(id=id)

    # Change status from 0 to 1
    leave.status = True

    # Save changes to database
    leave.save()

    return redirect("leave_list")


def attendance_add(request):

    # Check whether the form was submitted
    if request.method == "POST":

        # Get submitted attendance data
        form = AttendanceForm(request.POST)

        # Check whether the data is valid
        if form.is_valid():

            # Save attendance to database
            form.save()

            # Redirect to attendance list
            return redirect("attendance_list")

    else:

        # Display empty attendance form
        form = AttendanceForm()

    return render(
        request,
        "employees/attendance_add.html",
        {
            "form": form
        }
    )

def attendance_list(request):

    # Get all attendance records
    attendances = Attendance.objects.select_related(
        "employee"
    ).order_by("-date")

    return render(
        request,
        "employees/attendance_list.html",
        {
            "attendances": attendances
        }
    )