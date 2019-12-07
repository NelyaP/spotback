from django.shortcuts import render
from rest_framework import viewsets
from .models import Producer, Product, Order
from store.serializers import ProducerSerializer, ProductSerializer, OrderSerializer

class ProducerView(viewsets.ReadOnlyModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Views
def home(request):
    return render(request, 'index.html', {})


