
from django.urls import path, include



urlpatterns = [
    path('v1/employee/', include('employees.urls')),
]
