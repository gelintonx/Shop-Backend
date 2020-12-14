from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status
from rest_framework.response import Response
import stripe
from .payments import calculate_oreder

# Create your views here.

@api_view(['POST'])
def create_payment(request):
    items = [request.data]
    intent = stripe.PaymentIntent.create(
        amount = calculate_oreder(),
        currency = 'eur'
    )
    print(intent['client_secret'])

    return Response({"Hola":  "Todo OK"})