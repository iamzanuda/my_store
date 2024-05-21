from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Product
from favorites.models import Favorite
from review.models import Review
from cart_item.models import CartItem

from .pagination import ProductPagination

from .serializers import (ProductCardSerializer, ProductSerializer,
                          ReviewViewingSerializer, ProductInCartSerializer)


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

    def add_or_remove(self, request, model, product, message):
        """
        Add or remove a product from a user's favorite list or cart.
        """

        if request.method == 'POST':
            serializer = ProductInCartSerializer(
                product,
                data=request.data,
                context={'request': request}
            )
            serializer.is_valid(raise_exception=True)

            if product is None:
                return Response(
                    {'errors': 'Product does not exist.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not model.objects.filter(
                user=request.user,
                product=product
            ).exists():

                model.objects.create(user=request.user, product=product)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)

            return Response({'errors': 'Already in the list.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            if not model.objects.filter(user=request.user,
                                        product=product).exists():
                return Response({'errors': 'Product does not exist.'},
                                status=status.HTTP_400_BAD_REQUEST)

            get_object_or_404(model,
                              user=request.user,
                              product=product).delete()
            return Response({'detail': message},
                            status=status.HTTP_204_NO_CONTENT)

    @action(detail=True,
            methods=('POST', 'DELETE'),
            permission_classes=(IsAuthenticated,))
    def favorite(self, request, pk):
        """
        Add or remove a product from the favorite list.

        Accessible only to authenticated users.
        """

        product = get_object_or_404(Product, id=pk)
        return self.add_or_remove(request, Favorite, product,
                                  'Product removed from favorites.')

    @action(detail=True,
            methods=('POST', 'DELETE'),
            permission_classes=(IsAuthenticated,))
    def cart(self, request, pk):
        """
        Add or remove a product from the shopping cart.

        Accessible only to authenticated users.
        """

        product = get_object_or_404(Product, id=pk)
        return self.add_or_remove(request, CartItem, product,
                                  'Product removed from the cart.')


class ReviewViewingViewSet(viewsets.ModelViewSet):
    """
    Просмотр коментариев на странице конкретного продукта.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewViewingSerializer
