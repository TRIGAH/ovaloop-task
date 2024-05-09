from django.test import TestCase,Client
from django.urls import reverse,resolve
from product.models import Product
from product.views import CreateOrderViewSet,create_order
import json

class TestViews(TestCase):
    pass
     
    # def setUp(self):
    #     self.client = Client() 
    #     self.list_url = reverse('list')
    #     self.starfeeds = Product.objects.create(name="starfeeds",budget=200000)
    #     self.detail_url = reverse('detail',args=['starfeeds'])