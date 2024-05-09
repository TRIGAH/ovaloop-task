from django.test import TestCase,Client
from django.urls import reverse,resolve
from product.models import Product
from product.views import CreateOrderViewSet,create_order
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client() 
        self.post_url = reverse('create_order')
        self.product = Product.objects.create()

    def test_create_order_POST(self):
        response = self.client.post(self.post_url,{
            "id": "0d001705-fa00-4317-9bb0-f34118da491c",
            "business_name": "Ovaloop Venture",
            "quantity":"5",
            "name": "Fanta",
            "sku": "53418457",
            "cost_price": "4000.00",
            "selling_price": "6000.00",
            "stock_unit": "5",
            "unit_measurement": "Piece",
            "unit_increment": "1.00",
            "created_at": "2024-03-07T22:49:04.159536+01:00",
            "updated_at": "",
            "meta_measurement": [
            {
                "name": "Box",
                "base_quantity": "12",
                "selling_price": "29500",
                "full_name": "Box (12 qty)"
            },
            {
                "name": "Carton",
                "base_quantity": "12",
                "selling_price": "50500",
                "full_name": "Carton (12 qty)"
            }
            ]

        })
        self.assertEquals(response.status_code,201)


    
     