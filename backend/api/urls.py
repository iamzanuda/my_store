from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()

router.register('product', ProductViewSet, basename='product')
# router.register('review', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),

    # path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]
