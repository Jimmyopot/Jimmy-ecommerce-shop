from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('payment-option/<payment_option>', views.PaymentOptionView.as_view(), name='payment-option'),
] 