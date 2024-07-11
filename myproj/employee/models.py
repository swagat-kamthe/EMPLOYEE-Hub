from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    DeptID = models.BigIntegerField()
    ProjectID = models.BigIntegerField()
    ManagerID = models.BigIntegerField()



    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Department(models.Model):
    DeptName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.DeptName}"
    
class Manager(models.Model):
    ManagerName = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.ManagerName}"
    
class Project(models.Model):
    ProjectName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ProjectName}"
