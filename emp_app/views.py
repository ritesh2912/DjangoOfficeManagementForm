from django.shortcuts import render, HttpResponse
from .models import Member, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Member.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        phone = int(request.POST.get('phone'))
        dept_id = int(request.POST.get('dept'))
        role_id = int(request.POST.get('role'))
        
        if first_name and last_name and salary and bonus and phone and dept_id and role_id:
            try:
                dept = Department.objects.get(id=dept_id)
                role = Role.objects.get(id=role_id)
                
                new_emp = Member(
                    first_name=first_name,
                    last_name=last_name,
                    salary=salary,
                    bonus=bonus,
                    phone=phone,
                    dept=dept,
                    role=role,
                    hire_date=datetime.now()
                )
                new_emp.save()
                
                return HttpResponse('Member added Successfully')
            except (Department.DoesNotExist, Role.DoesNotExist):
                return HttpResponse('Invalid department or role')
        else:
            return HttpResponse('Please provide all the required information')
    elif request.method == 'GET':
        return render(request, 'view_add_emp.html')
    else:
        return HttpResponse("An Exception Occurred! Member Has Not Been Added")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Member.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Member Removed Successfully")
        except Member.DoesNotExist:
            return HttpResponse("Please Enter A Valid EMP ID")
    else:
        emps = Member.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'view_remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')

        emps = Member.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'view_filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
