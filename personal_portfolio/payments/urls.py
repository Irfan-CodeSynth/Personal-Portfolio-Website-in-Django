# payments/urls.py
from django.urls import path
from .views import CreateCheckoutSessionView, success, cancel

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]
