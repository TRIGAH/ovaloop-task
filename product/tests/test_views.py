from django.test import TestCase,Client
from django.urls import reverse,resolve
from product.models import Product
from product.views import CreateOrderViewSet,create_order
import json

class TestViews(TestCase):
    pass
     