from django.shortcuts import render
from .models import Employee
# Create your views here.

def empinfo(request):
    edata = Employee.objects.all()
    byname = Employee.objects.filter(ename__icontains='Sh')

    return render(request,'app/empdata.html',{'data':edata,'byname':byname})

def hello(request):
    return render(request,'app/2nd.html')
