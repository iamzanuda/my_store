from django.contrib import admin

from .models import Product, Size, Color


# Устанавливает заголовок, который будет отображаться
# на всех страницах административной панели.
admin.site.site_header = "my_store"

# Устанавливает название, которое будет отображаться
# в заголовке окна браузера.
admin.site.site_title = "my_store_title"

# Устанавливает заголовок, который будет отображаться
# на главной странице административной панели.
admin.site.index_title = "Добро пожаловать в администрирование my_store"


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    """
    Административная панель для управления размерами продуктов.

    Attributes:
        list_display (tuple): Поля модели, отображаемые в списке размеров.

    Examples:
        В административной панели вы можете:
            - Просматривать список размеров с полем 'size'.
    """

    list_display = ('size',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    """
    Административная панель для управления цветами продуктов.

    Attributes:
        list_display (tuple): Поля модели, отображаемые в списке цветов.

    Examples:
        В административной панели вы можете:
            - Просматривать список цветов с полем 'color'.
    """

    list_display = ('color',)


class ProductAdmin(admin.ModelAdmin):
    """
    Административная панель для управления продуктами.

    Attributes:
        list_display (tuple): Поля модели, отображаемые в списке продуктов.
        list_filter (tuple): Поля модели, используемые для фильтрации в
                             административной панели.
        search_fields (tuple): Поля модели, по которым можно
                               осуществлять поиск.
        filter_horizontal (tuple): Поля модели, представленные в виде
                                   горизонтальных фильтров
                                   (используется для полей ManyToMany).

    Examples:
        В административной панели вы можете:
            - Просматривать список продуктов с полями 'name',
                'current_price' и 'category'.
            - Фильтровать продукты по 'category', 'colors' и 'sizes'.
            - Искать продукты по 'name' и 'description'.
            - Управлять связями ManyToMany для полей 'sizes' и 'colors'.
    """

    list_display = ('name', 'current_price', 'category')
    list_filter = ('category', 'colors', 'sizes')
    search_fields = ('name', 'description')
    filter_horizontal = ('sizes', 'colors')


admin.site.register(Product, ProductAdmin)
