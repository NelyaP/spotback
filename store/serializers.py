from rest_framework import serializers
from store.models import Producer, Product, Order

class ProducerSerializer(serializers.ModelSerializer):
    """logo = serializers.SerializerMethodField()

    def get_logo(self, producer):
        request = self.context.get('request')
        logo_url = producer.logo.url
        return request.build_absolute_uri(logo_url)"""

    class Meta:
        model = Producer
        fields = ('id', 'name', 'description', 'rating', 'phone', 'url', 'logo')

class ProductSerializer(serializers.ModelSerializer):

    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'producer', 'name', 'description', 'price', 'photo', 'url')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product', 'creation_date', 'amount', 'status')