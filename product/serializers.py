from rest_framework import serializers
from .models import Product,MetaMeasurement,Order

products = [
  {
    "id": "0d001705-fa00-4317-9bb0-f34118da491c",
    "business_name": "Ovaloop Venture",
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
  },
  {
    "id": "0d001705-fa00-4317-9bb0-f34117da491c",
    "business_name": "Ovaloop Venture",
    "name": "Coke",
    "sku": "53418457",
    "cost_price": "2500.00",
    "selling_price": "4000.00",
    "stock_unit": "50",
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
  },
  {
    "id": "0d001705-fa00-4317-9bb0-f24118da491c",
    "business_name": "Ovaloop Venture",
    "name": "Sprite",
    "sku": "53418457",
    "cost_price": "2500.00",
    "selling_price": "4000.00",
    "stock_unit": "0",
    "unit_measurement": "Piece",
    "unit_increment": "1.00",
    "created_at": "2024-03-07T22:49:04.159536+01:00",
    "updated_at": "",
    "meta_measurement": [
      {
        "name": "Crate",
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
  },
  {
    "id": "0d001705-fa00-4317-9bb0-f35118da491c",
    "business_name": "Ovaloop Venture",
    "name": "Star",
    "sku": "53418457",
    "cost_price": "2500.00",
    "selling_price": "4000.00",
    "stock_unit": "100",
    "unit_measurement": "Piece",
    "unit_increment": "1.00",
    "created_at": "2024-03-07T22:49:04.159536+01:00",
    "updated_at": "",
    "meta_measurement": [
      {
        "name": "Crate",
        "base_quantity": "12",
        "selling_price": "12000",
        "full_name": "Box (12 qty)"
      },
      {
        "name": "Carton",
        "base_quantity": "12",
        "selling_price": "40500",
        "full_name": "Carton (12 qty)"
      }
    ]
  },
  {
    "id": "0d001405-fa00-4317-9bb0-f34118da491c",
    "business_name": "Ovaloop Venture",
    "name": "7up",
    "sku": "53418457",
    "cost_price": "250.00",
    "selling_price": "400.00",
    "stock_unit": "100",
    "unit_measurement": "Piece",
    "unit_increment": "1.00",
    "created_at": "2024-03-07T22:49:04.159536+01:00",
    "updated_at": "",
    "meta_measurement": [
      {
        "name": "Crate",
        "base_quantity": "12",
        "selling_price": "1500",
        "full_name": "Box (12 qty)"
      },
      {
        "name": "Carton",
        "base_quantity": "12",
        "selling_price": "10000",
        "full_name": "Carton (12 qty)"
      }
    ]
  }
]



class MetaMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model= MetaMeasurement
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    quantity = serializers.CharField(required=True)
    selling_price = serializers.CharField(required=True)
    meta_measurement = MetaMeasurementSerializer(required=False)
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','quantity','selling_price','meta_measurement','total_quantity']
        depth = 2


    def get_total_quantity(self, obj):
        print('THIS IS OBJ', obj)
        total_quantity = 0
        base_quantiy = obj['meta_measurement']['base_quantity']
        total_quantity = int(obj['quantity']) * int(base_quantiy)
        return total_quantity


class CreateOrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,required=True)

    class Meta:
        model = Order
        fields = ['products']
        depth = 2


    
    def create(self, validated_data):

            product_data = validated_data['products']

            valid_products = [product_payload for product_payload in product_data for product in products if str(product_payload['id'])== str(product['id'])]

            print("VALID PRODUCTS "*5 , valid_products)
            for product_obj in valid_products:
                try:
                    order = Order.objects.create(products=product_obj['id'])
                except Exception as e:  
                        raise serializers.ValidationError(f'could not create order {e}',e)      
            return order

        
    def validate(self,data):
        print('THIS DATA '*5 , data)
        for d in data['products']:
            if 'meta_measurement' in d:
                meta_measurement = d['meta_measurement']
                d['selling_price'] = meta_measurement.get('selling_price')
            if 'id' not in d:
                raise serializers.ValidationError('id field is required')    
            if 'selling_price' not in d:
                raise serializers.ValidationError('selling_price field is required')
            if 'quantity' not in d:
                raise serializers.ValidationError('quantity field is required')
        return data