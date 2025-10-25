


from django.urls import path

from employees import views





urlpatterns = [
    # Function-based URLs
    path('fbv/', views.create_employee, name='fbv-employee-list-create'),
    path('fbv/<int:pk>/', views.employee_detail, name='fbv-employee-detail'),

    # Class-based URLs
    path('cbv/', views.EmployeeListCreateView.as_view(), name='cbv-employee-list-create'),
    path('cbv/<int:pk>/', views.EmployeeDetailView.as_view(), name='cbv-employee-detail'),
    
]


