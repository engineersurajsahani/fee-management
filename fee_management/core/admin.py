from django.contrib import admin
from core.models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'batch', 'total_fee', 'paid_fee', 'balance_fee', 'is_full_paid')
    list_filter = ('department', 'batch', 'is_full_paid')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'department', 'batch', 'payment_date', 'payment_amount', 'payment_method')
    list_filter = ('department', 'batch', 'payment_method', 'payment_date')

@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('student', 'department', 'batch', 'scholarship_name', 'scholarship_issue_date', 'scholarship_amount')
    list_filter = ('department', 'batch', 'scholarship_name', 'scholarship_issue_date')