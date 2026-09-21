from django import forms
from .models import Employee
from .models import Attendance

class EmployeeForm(forms.ModelForm):


    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {

            "employee_id": forms.TextInput(attrs={
                "class": "form-control",
                "id": "employeeId"
            }),

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "id": "employeeName"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "id": "employeeEmail"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "id": "employeePhone"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select",
                "id": "employeeGender"
            }),

            "date_of_birth": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
                "id": "dateOfBirth"
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control",
                "id": "department"
            }),

            "designation": forms.TextInput(attrs={
                "class": "form-control",
                "id": "designation"
            }),

            "joining_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
                "id": "joiningDate"
            }),

            "employment_type": forms.Select(attrs={
                "class": "form-select",
                "id": "employmentType"
            }),

            "salary": forms.NumberInput(attrs={
                "class": "form-control",
                "id": "salary"
            }),

            "experience": forms.NumberInput(attrs={
                "class": "form-control",
                "id": "experience",
                "step": "0.1"
            }),

            "manager": forms.TextInput(attrs={
                "class": "form-control",
                "id": "manager"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "id": "address",
                "rows": 3
            }),

            "city": forms.TextInput(attrs={
                "class": "form-control",
                "id": "city"
            }),

            "state": forms.TextInput(attrs={
                "class": "form-control",
                "id": "state"
            }),

            "pincode": forms.TextInput(attrs={
                "class": "form-control",
                "id": "pincode"
            }),

            "status": forms.Select(attrs={
                "class": "form-select",
                "id": "status"
            }),

            "emergency_contact": forms.TextInput(attrs={
                "class": "form-control",
                "id": "emergencyContact"
            }),

            "message": forms.Textarea(attrs={
                "class": "form-control",
                "id": "message",
                "rows": 5
            }),
        }


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance

        fields = [
            "employee",
            "date",
            "status",
            "check_in",
            "check_out",
        ]

        widgets = {

            "employee": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "check_in": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time"
                }
            ),

            "check_out": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time"
                }
            ),
        }