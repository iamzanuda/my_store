from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CartViewSet, ProductViewSet, FavoritesViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'favorites', FavoritesViewSet, basename='favorites')


urlpatterns = [
    path('', include(router.urls)),
]
