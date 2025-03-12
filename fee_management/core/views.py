from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import *

# Create your views here.
@login_required
def student_dashboard(request):
    student = get_object_or_404(Student, user=request.user)
    payments = student.payments.all()
    return render(request, 'student_dashboard.html', {'student': student, 'payments': payments})

@login_required
def payment_history(request):
    student = get_object_or_404(Student, user=request.user)
    payments = student.payments.all()
    return render(request, 'payment_history.html', {'student': student, 'payments': payments})

@login_required
def make_payment(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))  # Convert to Decimal
        method = request.POST.get('method')
        if amount <= 0 or amount > student.balance_fee:
            messages.error(request, 'Invalid payment amount.')
            return redirect('make_payment')
        Payment.objects.create(student=student, department=student.department, batch=student.batch, payment_amount=amount, payment_method=method)
        messages.success(request, 'Payment successful!')
        return redirect('payment_history')
    return render(request, 'make_payment.html', {'student': student})

@login_required
def download_receipt(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id, student__user=request.user)
    return render(request, 'receipt.html', {'payment': payment})
