from django.shortcuts import render
from .models import Employee
# Create your views here.

def empinfo(request):
    edata = Employee.objects.all()

    return render(request,'app/empdata.html',{'data':edata})
