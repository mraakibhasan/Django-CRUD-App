from django.contrib import admin
from student.models import *

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'password', 'address')
