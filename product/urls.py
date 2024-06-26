from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateOrderViewSet,create_order

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('orders', CreateOrderViewSet)
 

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
