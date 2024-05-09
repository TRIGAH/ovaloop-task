from django.test import TestCase
from product.models import Product,MetaMeasurement


class TestModels(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(
            id = '0d001705-fa00-4317-9bb0-f34118da491c',
            selling_price = "50000",
            quantity = "4"
        )

    def  test_create_order_Slug_ON_SAVE(self):
        self.assertEquals(self.product1.selling_price,"50000")    

