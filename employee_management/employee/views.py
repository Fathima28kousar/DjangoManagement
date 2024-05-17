from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404


def employees(request):
    if request.method == 'POST':

        if not request.user.is_authenticated:
            messages.info(request, 'Please log in to add employee details')
            
        @login_required(login_url='/login/')
        def add_employee(request):
            data = request.POST
            employee_name = data.get('employee_name')
            employee_email = data.get('employee_email')
            employee_phone = data.get('employee_phone')
            employee_salary = data.get('employee_salary')
            employee_role = data.get('employee_role')
            employee_department = data.get('employee_department')
            employee_education = data.get('employee_education')
            employee_location = data.get('employee_location')
            employee_bonus = data.get('employee_bonus')
            employee_image = request.FILES.get('employee_image')

            Employee.objects.create(
                employee_name=employee_name,
                employee_email=employee_email,
                employee_phone=employee_phone,
                employee_salary=employee_salary,
                employee_role=employee_role,
                employee_department=employee_department,
                employee_image=employee_image,
                employee_education=employee_education,
                employee_location=employee_location,
                employee_bonus=employee_bonus,
            )
            return redirect('/viewAll/')
        return add_employee(request)
    queryset = Employee.objects.all()
    context = {'employee': queryset}
    
    return render(request, 'employee.html', context)

def view_employee(request):
    queryset = Employee.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(employee_name__icontains = request.GET.get('search'))

    context = {'employee': queryset}
    return render(request,'view.html',context)

@login_required(login_url='/login/')
def update(request,employee_name):
    try:
        queryset = Employee.objects.get(employee_name=employee_name)
    except Employee.DoesNotExist:
        raise Http404("Employee matching query does not exist.")

    if request.method == 'POST':
        data = request.POST
        employee_email = data.get('employee_email')
        employee_phone = data.get('employee_phone')
        employee_salary = data.get('employee_salary')
        employee_role = data.get('employee_role')
        employee_department = data.get('employee_department')
        employee_education = data.get('employee_education')
        employee_image = request.FILES.get('employee_image')

        queryset.employee_email = employee_email
        queryset.employee_phone = employee_phone
        queryset.employee_salary = employee_salary
        queryset.employee_role = employee_role
        queryset.employee_department = employee_department
        queryset.employee_education = employee_education
        if employee_image:
            queryset.employee_image = employee_image
        queryset.save()
        return redirect('/viewAll/')
    context = {'employee':queryset}
    return render(request,'update.html',context)

@login_required(login_url='/login/')
def delete(request,id):
    # print(id)
    queryset = Employee.objects.get(id = id)
    queryset.delete()
    return redirect('/viewAll/')


    
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/viewAll/')
    return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            messages.error(request,'Username is required')
            return redirect('/register/')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'Username already exists')
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        return redirect('/login/')
    return render(request,'register.html')

def singleEmployee(request, id):
    try:
        id = int(id)                    # Validate that 'id' is an integer
    except ValueError:
        return HttpResponse("Invalid ID") # If 'id' is not an integer, return a bad request response
    user = Employee.objects.filter(id=id).first()    # Attempt to retrieve the employee by ID
    context = {'user': user}                            # Render the template with the user context
    return render(request, 'single.html', context)

def home(request):
    return render(request,'home.html')