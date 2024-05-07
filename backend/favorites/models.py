from django.db import models

from product.models import Product
from users.models import CustomUser


class Favorite(models.Model):
    """
    Модель, описывающая избранные продукты для пользователя.

    Attributes:
        user (ForeignKey): Пользователь, к которому относится избранный
        продукт.
        product (ForeignKey): Избранный продукт.
    """

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=False,
        related_name='favorites',
        verbose_name='Пользователь',
        help_text='Пользователь, к которому относится избранный продукт',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Продукт',
        help_text='Избранный продукт',
    )

    class Meta:
        """
        Meta класс для определения метаданных модели.

        Если вам нужно изменить имя или язык таблицы
        в административной панели, раскомментируйте строки:
        -> verbose_name = ''
        -> verbose_name_plural = ''
        """

        # verbose_name = 'Избранное'
        # verbose_name_plural = 'Избранное'

    def __str__(self):
        """
        Возвращает имя пользователя и название продукта.
        """

        return f'{self.user.username} - {self.product.name}'
