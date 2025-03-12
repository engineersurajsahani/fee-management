from django.db import models
from django.contrib.auth.models import User

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.CharField(max_length=10)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    paid_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_full_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.balance_fee = self.total_fee - self.paid_fee
        self.is_full_paid = self.balance_fee == 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

# Payment Model
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.CharField(max_length=10)
    payment_date = models.DateField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=[('CASH', 'Cash'), ('ONLINE', 'Online')])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.student.paid_fee += self.payment_amount
        self.student.save()

# Scholarship Model
class Scholarship(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.CharField(max_length=10)
    scholarship_name = models.CharField(max_length=255)
    scholarship_issue_date = models.DateField()
    scholarship_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.student.paid_fee += self.scholarship_amount
        self.student.save()