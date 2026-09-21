from django.db import models

# Create your models here.
class Employee(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Contract", "Contract"),
        ("Intern", "Intern"),
        ("Freelancer", "Freelancer"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("On Leave", "On Leave"),
        ("Resigned", "Resigned"),
        ("Terminated", "Terminated"),
    ]

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True
)

    designation = models.CharField(max_length=100)

    joining_date = models.DateField()

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    experience = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    manager = models.CharField(max_length=100)

    address = models.TextField()

    city = models.CharField(max_length=50)

    state = models.CharField(max_length=50)

    pincode = models.CharField(max_length=6)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    emergency_contact = models.CharField(
        max_length=10
    )

    message = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


   ####   Department model
class Department(models.Model):
    department_id = models.CharField(max_length=20, unique=True)
    department_name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name

class Leave(models.Model):
    
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    reason = models.TextField(blank=True)
    from_date = models.DateField() 
    to_date = models.DateField()
    manager = models.CharField(max_length=20)
    leave_type = models.CharField(max_length=30)
     # 0 = Pending
    # 1 = Approved
    status = models.BooleanField(default=False)

    def __str__(self):
     return str(self.employee_id)


class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    STATUS_CHOICES = (
        ("P", "Present"),
        ("A", "Absent"),
        ("H", "Half Day"),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES
    )

    check_in = models.TimeField(
        null=True,
        blank=True
    )

    check_out = models.TimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.employee} - {self.date}"


