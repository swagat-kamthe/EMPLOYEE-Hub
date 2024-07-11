from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee,Department,Manager,Project
from .forms import EmployeeForm,DepartmentForm,ManagerForm,ProjectForm

def employee_list(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    managers = Manager.objects.all()
    projects = Project.objects.all()

    selected_department = request.POST.get('department', '')
    selected_manager = request.POST.get('manager', '')
    selected_project = request.POST.get('project', '')
    name_query = request.POST.get('name', '')

    if selected_department:
        employees = employees.filter(DeptID=selected_department)
    if selected_manager:
        employees = employees.filter(ManagerID=selected_manager)
    if selected_project:
        employees = employees.filter(ProjectID=selected_project)
    if name_query:
        employees = employees.filter(first_name__icontains=name_query) | employees.filter(last_name__icontains=name_query)

    table_visibility = request.POST.get('table_visibility', 'hide')

    context = {
        'employees': employees,
        'departments': departments,
        'managers': managers,
        'projects': projects,
        'selected_department': selected_department,
        'selected_manager': selected_manager,
        'selected_project': selected_project,
        'name_query': name_query,
        'table_visibility': table_visibility,
    }

    return render(request, 'employee_list.html', context)


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})


#------------------------------------------Department----------------------------------------------------------

def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'department_detail.html', {'department': department})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        return redirect('employee_list')
    return render(request, 'department_confirm_delete.html', {'department': department})


#------------------------------------------Manager----------------------------------------------------------

def manager_create(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = ManagerForm()
    return render(request, 'manager_form.html', {'form': form})

def manager_detail(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    return render(request, 'manager_detail.html', {'manager': manager})

def manager_update(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = ManagerForm(instance=manager)
    return render(request, 'manager_form.html', {'form': form})

def manager_delete(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    if request.method == "POST":
        Manager.delete()
        return redirect('employee_list')
    return render(request, 'manager_confirm_delete.html', {'manager': manager})


#------------------------------------------Project----------------------------------------------------------

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        Project.delete()
        return redirect('employee_list')
    return render(request, 'project_confirm_delete.html', {'project': project})
