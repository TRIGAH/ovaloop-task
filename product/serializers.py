from rest_framework import serializers
from .models import Product,MetaMeasurement


class MetaMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model= MetaMeasurement
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    quantity = serializers.CharField(required=True)
    selling_price = serializers.CharField(required=True)
    meta_measurement = MetaMeasurementSerializer(required=False)
    class Meta:
        model = Product
        fields = ['id','quantity','selling_price','meta_measurement']




class CreateOrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,required=True)
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'


    def get_total_quantity(self, obj):
        total_quantity = 0
        base_quantiy = self.validated_data['meta_measurement'][0]['base_quantity']
        total_quantity = int(self.validated_data['quantity']) * int(base_quantiy)
        return total_quantity
    
    def create(self, validated_data):
        print("THIS IS VALID_DATA "*5,validated_data)
        product_data = validated_data['products'][0]
        meta_measurement_data = product_data.pop('meta_measurement')
        if 'meta_measurement' in product_data:
            try:
                print('PRODUCT DATA '*5 , product_data)
                print('META DATA '*5 , meta_measurement_data)
                product = Product.objects.create(**product_data)
                meta_measurement = MetaMeasurement.objects.create(**meta_measurement_data)
                product.meta_measurement.add(meta_measurement)
            except Exception as e:  
                raise serializers.ValidationError('coul not create product',e)      
        else:
            product = Product.objects.create(**product_data)
        return product

        
    # def validate(self,data):
    #     print("THIS IS DATA"*10,data)
    #     if 'meta_measurement' in data:
    #         meta_measurement = data['meta_measurement']
    #         data['selling_price'] = meta_measurement[0].get('selling_price')
    #     if 'id' not in data['products'][0]:
    #         raise serializers.ValidationError('id field is required')    
    #     if 'selling_price' not in data['products'][0]:
    #         raise serializers.ValidationError('selling_price field is required')
    #     if 'quantity' not in data['products'][0]:
    #         raise serializers.ValidationError('quantity field is required')
    #     return data