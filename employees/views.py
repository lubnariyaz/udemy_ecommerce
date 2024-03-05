from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from employees.models import Employee

# Create your views here.

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    # return HttpResponse(employee)
    return render(request, 'employee_detail.html')
    