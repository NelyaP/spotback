from rest_framework import serializers
from store.models import Producer, Product, Order

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('id', 'name', 'description', 'rating', 'phone', 'url', 'logo')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'producer', 'name', 'description', 'price', 'photo', 'url')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product', 'creation_date', 'amount', 'status')