from django.shortcuts import render
"""
from rest_frameworks import status
from rest_frameworks.response import Response
from rest_frameworks.decorators import api_view

from .models import Producer, Product, Order
from store.serializers import ProducerSerializer, ProductSerializer, OrderSerializer
"""

# Views
def home(request):
    return render(request, 'index.html', {})

"""
@api_view(['GET', ])
def api_product_view(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)"""

