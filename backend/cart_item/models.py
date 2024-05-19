from django.db import models

from product.models import Product
from users.models import CustomUser


class CartItem(models.Model):
    """
    Модель, описывающая товар в корзине покупателя.

    Attributes:
        user (ForeignKey): Пользователь, к которому относится продукт.
        product (ForeignKey): Продукт, добавленный в корзину.
        quantity (IntegerField): Количество данного продукта в корзине.
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
        Meta класс для определения метаданных модели.

        Если вам нужно изменить имя или язык таблицы
        в административной панели, раскомментируйте строки:
        -> verbose_name = ''
        -> verbose_name_plural = ''
        """

        # verbose_name = 'Элемент корзины'
        # verbose_name_plural = 'Элементы корзины'

    def __str__(self):
        """
        Возвращает название продукта и количество в корзине.
        """

        return f'{self.product.name} - {self.quantity}'
