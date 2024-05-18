from django.db import models


class Product(models.Model):
    """
    Модель, описывающая продукт.

    Attributes:
        name (str): Название продукта.
        image (str): Изображение продукта.
        description (str): Описание продукта.
        current_price (Decimal): Текущая цена.
        old_price (Decimal): Старая цена.
        sizes (str): Размеры продукта.
        colors (str): Цвета продукта.
        category (str): Категория продукта
            (Футболка, брюки, шорты и т.д.).
    """

    CATEGORIES = (
        ('T-shirts', 'Футболки'),
        ('Trousers', 'Брюки'),
        ('Shorts', 'Шорты'),
        ('Hoodie', 'Худи'),
    )

    COLORS = (
        ('Gray', 'Серый'),
        ('Black', 'Чёрный'),
        ('White', 'Белый'),
        ('Red', 'Красный'),
    )

    SIZES = (
        ('S', 'S, EUR: 38, RUS 44'),
        ('M', 'M, EUR: 40, RUS 46'),
        ('L', 'L, EUR: 42, RUS 48'),
        ('XL', 'XL, EUR: 44, RUS 50'),
    )

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
    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Текущая цена',
        help_text='Текущая цена продукта',
    )
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Старая цена',
        help_text='Старая цена продукта',
    )
    sizes = models.CharField(
        max_length=50,
        choices=SIZES,
        verbose_name='Размеры',
        help_text='Размеры продукта',
    )
    colors = models.CharField(
        max_length=50,
        choices=COLORS,
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
