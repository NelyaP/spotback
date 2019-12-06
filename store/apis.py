from django.http import JsonResponse

from .models import Producer, Product, Order
from store.serializers import ProducerSerializer, ProductSerializer, OrderSerializer

def get_producers(request):
    producers = ProducerSerializer(
        Producer.objects.all().order_by('-id'),
        many=True,
        context={'request': request}
    ).data
    return JsonResponse( {'producers': producers} )

def get_producer(request, producer_id):
    producer = ProducerSerializer(
        Producer.objects.all().filter(id=producer_id),
        many=True,
        context={'request': request}
    ).data
    return JsonResponse( {'producer': producer} )

def get_products(request):
    products = ProductSerializer(
        Product.objects.all(),
        many=True
    ).data
    print(products)
    return JsonResponse( {'products': products} )

def get_product(request, product_id):
    product = ProductSerializer(
        Product.objects.all().filter(id=product_id),
        many=True
    ).data
    return JsonResponse( {'product': product} )

def get_orders(request):
    orders = OrderSerializer(
        Order.objects.all().order_by('-id'),
        many=True
    ).data
    return JsonResponse( {'orders': orders} )