from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
