from rest_framework import viewsets

from product.models import Product
from review.models import Review

from .pagination import ProductPagination
from .serializers import (ProductCardSerializer, ProductSerializer,
                          ReviewViewingSerializer)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing products. Provides 'list' and 'retrieve' actions.

    This viewset automatically provides `list` and `retrieve` actions.
    It uses different serializers for the 'list' and 'retrieve' actions.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action.

        Uses ProductSerializer for the 'list' action and ProductCardSerializer
        for the 'retrieve' action.
        """

        if self.action == 'list':
            return ProductSerializer
        return ProductCardSerializer


class ReviewViewingViewSet(viewsets.ModelViewSet):
    """
    Просмотр коментариев на странице конкретного продукта.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewViewingSerializer
