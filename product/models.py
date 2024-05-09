from django.db import models
import uuid
from datetime import timezone
# Create your models here.

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

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
         return f"{self.name}"
    
