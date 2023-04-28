from django.contrib import admin
from django.urls import path
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentRegister,name='home'),
    path('delete/<int:id>', deleteStudent, name='deletestudent'),
    path('update/<int:id>/', updateStudent, name='update_student'),
]
