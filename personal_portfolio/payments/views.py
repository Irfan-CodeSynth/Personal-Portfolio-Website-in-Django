from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        plan = request.POST.get('plan')

        # Use actual price IDs here
        prices = {
            'basic': 'price_1PZz34KU5ElamTokxi841FFZ', 
            'standard': 'price_1PZz4YKU5ElamTokU6fPCTWl',
            'silver': 'price_1PZz5gKU5ElamTokdrlMnE6b'
        }

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': prices[plan],
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN + '/payments/success/',
            cancel_url=YOUR_DOMAIN + '/payments/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id,
            'url': checkout_session.url
        })

# Your success and cancel views
def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')
