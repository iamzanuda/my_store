from rest_framework import serializers

from review.models import Review
from product.models import Product, Color, Size
from users.models import CustomUser
from cart_item.models import CartItem
from favorites.models import Favorite
from order.models import Order


#---------------ORDER------------------------------------
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
    Serializer for viewing comments on the product detail page.

    Attributes:
        user (StringRelatedField): Displays the user's name as
            specified in the model's __str__ method.
        text (str): The text of the review.
        rating (int): The rating given by the user.
        created_at (datetime): The date and time when the review was created.
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


class SizeSerializer(serializers.ModelSerializer):
    """
    Serializer for representing the size of the product.

    Attributes:
        size (str): The size of the product.
    """

    class Meta:
        model = Size
        fields = (
            'size',
        )


class ColorSerializer(serializers.ModelSerializer):
    """
    Serializer for representing the color of the product.

    Attributes:
        color (str): The color of the product.
    """

    class Meta:
        model = Color
        fields = (
            'color',
        )


class ProductCardSerializer(serializers.ModelSerializer):
    """
    Serializer for representing the product details on the product page.

    Attributes:
        name (str): The name of the product.
        image (str): The image URL of the product.
        description (str): The description of the product.
        current_price (Decimal): The current price of the product.
        sizes (SizeSerializer): The sizes available for the product.
        colors (ColorSerializer): The colors available for the product.
        category (str): The category of the product.
        reviews (ReviewViewingSerializer): The reviews related to the product.
    """

    reviews = ReviewViewingSerializer(read_only=True, many=True)
    sizes = SizeSerializer(read_only=True, many=True)
    colors = ColorSerializer(read_only=True, many=True)

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


#----FAVORITE--------------------------------------------------
class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for representing a user's favorite products.

    Attributes:
        user (str): The user who marked the product as favorite. 
            This field is read-only and displays the user's name 
            or identifier.
        product (ProductSerializer): The detailed information of the product 
            marked as favorite. 
            This field is read-only and uses the ProductSerializer to serialize 
            the product details.
    """

    user = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = (
            'user',
            'product',
        )


#----CART--------------------------------------------------
class ProductInCartSerializer(serializers.ModelSerializer):
    """
    Serializer for representing the product details within the cart.

    Attributes:
        name (str): The name of the product.
        image (str): The image URL of the product.
        current_price (Decimal): The current price of the product.
        sizes (SizeSerializer): The sizes available for the product.
        colors (ColorSerializer): The colors available for the product.
        category (str): The category of the product.
    """

    sizes = SizeSerializer(read_only=True, many=True)
    colors = ColorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            'name',
            'category',
            'image',
            'current_price',
            'sizes',
            'colors',
        )
        read_only_fields = (
            'name',
            'category',
            'image',
            'current_price',
            'sizes',
            'colors',
        )


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for representing the cart item details.

    Attributes:
        user (ForeignKey): The user who added the product to the cart.
        product (ProductInCartSerializer): The product added to the cart.
        quantity (int): The quantity of the product in the cart.
    """

    user = serializers.StringRelatedField(read_only=True)
    product = ProductInCartSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = (
            'user',
            'product',
            'quantity',
        )
        read_only_fields = (
            'user',
            'product',
            'quantity',
        )


# ----USER----------------------------------------------
class CustomUserSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            )