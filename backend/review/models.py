from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from product.models import Product
from users.models import CustomUser


class Review(models.Model):
    """
    Модель, описывающая отзыв о продукте.

    Attributes:
        user (ForeignKey): Пользователь, оставивший отзыв.
        product (ForeignKey): Продукт, к которому относится отзыв.
        text (TextField): Текст отзыва.
        rating (IntegerField): Оценка, которую пользователь поставил продукту.
        created_at (DateTimeField): Дата и время создания отзыва.
    """

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Пользователь',
        help_text='Пользователь, оставивший отзыв',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Продукт',
        help_text='Продукт, к которому относится отзыв',
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Текст отзыва о продукте',
    )
    rating = models.PositiveIntegerField(
        default=10,
        validators=(
            MinValueValidator(1),
            MaxValueValidator(5),
        ),
        verbose_name='Оценка',
        help_text='Оценка, которую пользователь поставил продукту',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания отзыва',
        help_text='Дата и время создания отзыва',
    )

    class Meta:
        """
        Meta класс для определения метаданных модели.

        Если вам нужно изменить имя или язык таблицы
        в административной панели, раскомментируйте строки:
        -> verbose_name = ''
        -> verbose_name_plural = ''
        """

        # verbose_name = 'Отзыв'
        # verbose_name_plural = 'Отзывы'

    def __str__(self):
        """
        Возвращает название пользователя и продукта, к которому относится
        отзыв.
        """

        return f'{self.user.username} - {self.product.name}'
