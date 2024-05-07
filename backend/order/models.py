from django.db import models

from product.models import Product
from users.models import CustomUser


class Order(models.Model):
    """
    Модель, описывающая заказ пользователя.

    Attributes:
        products (ManyToManyField): Список продуктов, входящих в заказ.
        user (ForeignKey): Пользователь, оформивший заказ.
        status (CharField): Статус заказа (обрабатывается, доставляется,
          завершен и т.д.).
        created_at (DateTimeField): Дата и время создания заказа.
    """

    products = models.ManyToManyField(
        Product,
        related_name='orders',
        verbose_name='Продукты',
        help_text='Список продуктов, входящих в заказ',
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Пользователь',
        help_text='Пользователь, оформивший заказ',
    )
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказа',
        help_text='Статус заказа (обрабатывается, доставляется, и т.д.)',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заказа',
        help_text='Дата и время создания заказа',
    )

    class Meta:
        """
        Meta класс для определения метаданных модели.

        Если вам нужно изменить имя или язык таблицы
        в административной панели, раскомментируйте строки:
        -> verbose_name = ''
        -> verbose_name_plural = ''
        """

        # verbose_name = 'Заказ'
        # verbose_name_plural = 'Заказы'

    def __str__(self):
        """
        Возвращает название пользователя и дату создания заказа.
        """

        return f'{self.user.username} - {self.created_at}'
