from django.db import models
from django.utils import timezone #timezone.now()

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    url = models.URLField()
    logo = models.ImageField('Logo', upload_to='store/photos/producers', default='', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField(default=0)
    photo = models.ImageField('Photo', upload_to='store/photos/products', default='', blank=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

#class Bag(models.Model):
    #size = models.CharField(max_length=10), color, photo

class Order(models.Model):
    creation_date = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    status = models.CharField(max_length=150)
