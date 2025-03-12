from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', student_dashboard, name='student_dashboard'),
    path('payment-history/', payment_history, name='payment_history'),
    path('make-payment/', make_payment, name='make_payment'),
    path('download-receipt/<int:payment_id>/', download_receipt, name='download_receipt'),
]
