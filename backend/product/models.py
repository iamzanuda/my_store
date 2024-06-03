from django.db import models


class Size(models.Model):
    """
    Модель, описывающая размер продукта.
    """

    SIZE_CHOICES = (
        ('S, EUR: 38, RUS 44', 'S, EUR: 38, RUS 44'),
        ('M, EUR: 40, RUS 46', 'M, EUR: 40, RUS 46'),
        ('L, EUR: 42, RUS 48', 'L, EUR: 42, RUS 48'),
        ('XL, EUR: 44, RUS 50', 'XL, EUR: 44, RUS 50'),
    )

    size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES,
        verbose_name='Размер',
        help_text='Размер продукта',
        unique=True,
    )

    def __str__(self):
        return self.size


class Color(models.Model):
    """
    Модель, описывающая цвет продукта.
    """

    COLOR_CHOICES = (
        ('Серый', 'Серый'),
        ('Чёрный', 'Чёрный'),
        ('Белый', 'Белый'),
        ('Красный', 'Красный'),
    )

    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        verbose_name='Цвет',
        help_text='Цвет продукта',
        unique=True,
    )

    def __str__(self):
        return self.color


class Product(models.Model):
    """
    Модель, описывающая продукт.

    Attributes:
        name (str): Название продукта.
        image (str): Изображение продукта.
        description (str): Описание продукта.
        current_price (Decimal): Текущая цена.
        old_price (Decimal): Старая цена.
        sizes (ManyToManyField): Размеры продукта.
        colors (ManyToManyField): Цвета продукта.
        category (str): Категория продукта
            (Футболка, брюки, шорты и т.д.).
    """

    CATEGORIES = (
        ('T-shirts', 'Футболки'),
        ('Trousers', 'Брюки'),
        ('Shorts', 'Шорты'),
        ('Hoodie', 'Худи'),
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
    sizes = models.ManyToManyField(
        Size,
        verbose_name='Размеры',
        help_text='Размеры продукта',
    )
    colors = models.ManyToManyField(
        Color,
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
        """

        # verbose_name = 'Продукт'
        # verbose_name_plural = 'Продукты'

    def __str__(self):
        """
        Возвращает название продукта.
        """
        return self.name
