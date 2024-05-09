from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import CreateOrderSerializer
from product.models import Product,MetaMeasurement
from rest_framework import viewsets
from rest_framework import status


# Create your views here.




class CreateOrderViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateOrderSerializer



@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        serializer = CreateOrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()    

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


products_list = [
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
    "id": "0d001705-fa00-4317-9bb0-f34118da491c",
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
    "id": "0d001705-fa00-4317-9bb0-f34118da491c",
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
    "id": "0d001705-fa00-4317-9bb0-f34118da491c",
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
    "id": "0d001705-fa00-4317-9bb0-f34118da491c",
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



# @api_view(['GET', 'POST'])
# def create_order(request):
#     if request.method == 'POST':
#         # id = request.data.get('id')
#         # selling_price = request.data.get('selling_price')
#         # quantity = request.data.get('quantity')
#         orderitems = [Orders(**item) for item in products_list ]
#         orders=Orders.objects.bulk_create(orderitems)
#         serializer = CreateOrderSerializer(data=orders, many=True)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({"message": "Order Created Successfully", "data":serializer.data})
        
#     return Response({"message": request.data})













