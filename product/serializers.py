from rest_framework import serializers
from .models import Product,MetaMeasurement


class MetaMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model= MetaMeasurement
        fields = '__all__'

class CreateOrderSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    quantity = serializers.CharField(required=True)
    selling_price = serializers.CharField(required=True)
    total_quantity = serializers.SerializerMethodField()
    meta_measurement = MetaMeasurementSerializer(many=True,required=False)

    class Meta:
        model = Product
        fields = '__all__'


    def get_total_quantity(self, obj):
        total_quantity = 0
        base_quantiy = self.validated_data['meta_measurement'][0]['base_quantity']
        total_quantity = int(self.validated_data['quantity']) * int(base_quantiy)
        return total_quantity
    
    def create(self, validated_data):
        if 'meta_measurement' in validated_data:
            meta_measurement_data = validated_data.pop('meta_measurement')
            try:
                product = Product.objects.create(**validated_data)
                for mm_data in meta_measurement_data:
                    meta_measurement, _ = MetaMeasurement.objects.get_or_create(**mm_data)
                    product.meta_measurement.add(meta_measurement)
            except Exception as e:  
                raise serializers.ValidationError('coul not create product',e)      
        else:
            product = Product.objects.create(**validated_data)
        return product

        
    def validate(self,data):
        if 'meta_measurement' in data:
            meta_measurement = data['meta_measurement']
            data['selling_price'] = meta_measurement[0].get('selling_price')
        if 'id' not in data:
            raise serializers.ValidationError('id field is required')    
        if 'selling_price' not in data:
            raise serializers.ValidationError('selling_price field is required')
        if 'quantity' not in data:
            raise serializers.ValidationError('quantity field is required')
        return data