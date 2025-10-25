from .models import Employee


def create_employee_service(validated_data):
  
    # Handles creation of a new employee.
    
    employee = Employee.objects.create(**validated_data)
    return employee


def update_employee_service(employee, validated_data):
    # Handles updating of an existing employee.
  
    for attr, value in validated_data.items():
        setattr(employee, attr, value)
    employee.save()
    return employee


def delete_employee_service(employee):
    
    # Handles deletion of an employee.
  
    employee.delete()
    return True
