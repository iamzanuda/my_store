from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CartViewSet, ProductViewSet, FavoriteViewSet

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'favorites', FavoriteViewSet, basename='favorites')


urlpatterns = [
    path('', include(router.urls)),
]
