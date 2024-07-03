from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CartItemViewSet, ProductViewSet, FavoriteViewSet

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')
router.register(r'cart', CartItemViewSet, basename='cart')
router.register(r'favorite', FavoriteViewSet, basename='favorite')


urlpatterns = [
    path('', include(router.urls)),
]
