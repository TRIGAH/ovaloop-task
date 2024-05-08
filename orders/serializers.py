from rest_framework import serializers
from .models import Orders,MetaElement

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'