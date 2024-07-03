from django.db import models

from product.models import Product
from users.models import CustomUser


class CartItem(models.Model):
    """
    Model describing an item in a customer's shopping cart.

    Attributes:
        user (ForeignKey): The user to whom the product belongs.
        product (ForeignKey): The product added to the cart.
        quantity (IntegerField): The quantity of the product in the cart.
    """

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=False,
        related_name='cart_items',
        verbose_name='Пользователь',
        help_text='Пользователь, к которому относится продукт',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='Продукт',
        help_text='Продукт, добавленный в корзину',
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name='Количество',
        help_text='Количество данного продукта в корзине',
    )

    class Meta:
        """
        Meta class to define model metadata.

        If you need to change the name or language of the table
        in the admin panel, uncomment the lines:
        -> verbose_name = ''
        -> verbose_name_plural = ''
        """

        # verbose_name = 'Элемент корзины'
        # verbose_name_plural = 'Элементы корзины'

    def __str__(self):
        """
        Returns the product name and quantity in the cart.
        """

        return f'{self.product.name} - {self.quantity}'
