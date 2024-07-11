from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    #-----------------------------------Department----------------------------------------------

    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('department/new/', views.department_create, name='department_create'),
    path('department/<int:pk>/edit/', views.department_update, name='department_update'),
    path('department/<int:pk>/delete/', views.department_delete, name='department_delete'),

    #-----------------------------------Manager----------------------------------------------

    path('manager/<int:pk>/', views.manager_detail, name='manager_detail'),
    path('manager/new/', views.manager_create, name='manager_create'),
    path('manager/<int:pk>/edit/', views.manager_update, name='manager_update'),
    path('manager/<int:pk>/delete/', views.manager_delete, name='manager_delete'),

   #-----------------------------------Project----------------------------------------------

    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
]
