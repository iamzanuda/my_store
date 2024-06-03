from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')
# router.register('review', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),
]
