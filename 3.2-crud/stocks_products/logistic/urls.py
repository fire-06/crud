
from django.urls import path, include
from logistic.views import ProductViewSet, StockViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
