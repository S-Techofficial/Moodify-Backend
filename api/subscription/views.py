from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import braintree
import os

# Create your views here.

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=os.getenv('PAYMENT_MERCHANT_ID'),
        public_key=os.getenv('PAYMENT_PUBLIC_KEY'),
        private_key=os.getenv('PAYMENT_PRIVATE_KEY')
    )
)


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid Session, Please Login Again!'})
    return JsonResponse({'clientToken': gateway.client_token.generate(), 'success': True})


@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid Session, Please Login Again!'})

    nonce_from_the_client = request.POST['paymentMethodNonce']
    plan_id_from_the_client = request.POST['planId']

    result = gateway.subscription.create({
        "payment_method_nonce": nonce_from_the_client,
        "plan_id": plan_id_from_the_client,
        "options": {
            "start_immediately": True
        }
    })

    if result.is_success:
        return JsonResponse({
            'success': result.is_success, 'subscription': {'status': result.subscription.Status, 'plan': result.subscription.price}
        })
    else:
        return JsonResponse({'error': True, 'success': False})
