from django.db import models


class Product(models.Model):
    """
    Модель, описывающая продукт.

    Attributes:
        name (str): Название продукта.
        image (str): Изображение продукта.
        description (str): Описание продукта.
        price (Decimal): Цена продукта.
        sizes (str): Размеры продукта.
        colors (str): Цвета продукта.
        category (str): Категория продукта
            (Футболка, брюки, шорты и т.д.).
    """

    CATEGORIES = [
        ('T-shirts', 'Футболки'),
        ('Trousers', 'Брюки'),
        ('Shorts', 'Шорты'),
        ('Hoodie', 'Худи'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Название продукта',
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение товара',
        help_text='Загрузите изображение товара',
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Описание',
        help_text='Описание продукта',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        help_text='Цена продукта',
    )
    sizes = models.CharField(
        max_length=50,
        verbose_name='Размеры',
        help_text='Размеры продукта',
    )
    colors = models.CharField(
        max_length=50,
        verbose_name='Цвета',
        help_text='Цвета продукта',
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
        verbose_name='Категория',
        help_text='Категория продукта',
    )

    class Meta:
        """
        Meta класс для определения метаданных модели.

        Если вам нужно изменить имя или язык таблицы
        в административной панели, раскомментируйте строки:
        -> verbose_name = ''
        -> verbose_name_plural = ''
        """

        # verbose_name = 'Продукт'
        # verbose_name_plural = 'Продукты'

    def __str__(self):
        """
        Возвращает название продукта.
        """

        return self.name
