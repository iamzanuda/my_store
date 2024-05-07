from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet
from product.views import ProductViewSet

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')
router.register('product', ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),

    # path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]
