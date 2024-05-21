from rest_framework import serializers

from review.models import Review
from product.models import Product
from users.models import CustomUser
from cart_item.models import CartItem
from favorites.models import Favorite
from order.models import Order


class ProductInCartSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Product
        fields = (
                  'name',
                  'image',
                  'current_price',
                  'sizes',
                  'colors',
                  'category',
                  )


class CartItemSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = CartItem
        fields = (
                  'user',
                  'product',
                  'quantity',
                  )


class FavoriteSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Favorite
        fields = (
                  'user',
                  'product',
                  )


class OrderSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Order
        fields = (
                  'products',
                  'user',
                  'status',
                  'created_at',
                  )


# Product------------------------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Product
        fields = (
                  'id',
                  'name',
                  'image',
                  'current_price',
                  )


# Review-Product-----------------------------------------------------------------
class ReviewViewingSerializer(serializers.ModelSerializer):
    """
    Для просмотра коментариев на детальной странице продукта.

    StringRelatedField выводит то что указанно в def __str__ модели,
    в данном случае имя юзера.
    """

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = (
                  'user',
                  'text',
                  'rating',
                  'created_at',
                  )


class ProductCardSerializer(serializers.ModelSerializer):
    """

    Поле reviews связанно с моделью Review и ReviewListSerializer
    с его помощью выводим информацию об отзывах на страницу товара.
    """

    reviews = ReviewViewingSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
                  'name',
                  'image',
                  'description',
                  'current_price',
                  'sizes',
                  'colors',
                  'category',
                  'reviews',
                  )


# User----------------------------------------------------------------------------
class CustomUserSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = CustomUser
        fields = (
                  'email',
                  'password',
                  )
