from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "employees/dashboard.html")

def forms(request):
    return render(request, "employees/forms.html")