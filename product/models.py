from django.db import models
import uuid
from datetime import timezone
# Create your models here.

#   {
#     "id": "0d001705-fa00-4317-9bb0-f34118da491c",
#     "business_name": "Ovaloop Venture",
#     "name": "Fanta",
#     "sku": "53418457",
#     "cost_price": "4000.00",
#     "selling_price": "6000.00",
#     "stock_unit": "5",
#     "unit_measurement": "Piece",
#     "unit_increment": "1.00",
#     "created_at": "2024-03-07T22:49:04.159536+01:00",
#     "updated_at": "",
#     "meta_measurement": [
#       {
#         "name": "Box",
#         "base_quantity": "12",
#         "selling_price": "29500",
#         "full_name": "Box (12 qty)"
#       },
#       {
#         "name": "Carton",
#         "base_quantity": "12",
#         "selling_price": "50500",
#         "full_name": "Carton (12 qty)"
#       }
#     ]
#   },

class MetaMeasurement(models.Model):
    name = models.CharField(max_length=100)
    base_quantity = models.CharField(max_length=100)
    selling_price = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    business_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100,blank=True,null=True)
    sku = models.CharField(max_length=100,blank=True,null=True)
    cost_price = models.CharField(max_length=100,blank=True,null=True)
    stock_unit = models.CharField(max_length=100,blank=True,null=True)
    unit_measurement = models.CharField(max_length=100,blank=True,null=True)
    unit_increment = models.CharField(max_length=100,blank=True,null=True)
    selling_price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    meta_measurement = models.ManyToManyField(MetaMeasurement)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f"{self.name}"
    
