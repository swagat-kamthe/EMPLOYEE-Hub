from django import forms
from .models import Employee,Department,Manager,Project

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'position','addr','DeptID','ProjectID','ManagerID']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['DeptName']
    
class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['ManagerName']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['ProjectName']