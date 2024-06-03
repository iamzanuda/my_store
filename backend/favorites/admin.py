from django.contrib import admin

from .models import Favorite


class FavoriteAdmin(admin.ModelAdmin):
    """
    Административная панель для управления избранным.

    Attributes:
        list_display (tuple): Поля модели, отображаемые в списке избранного.

    Examples:
        В административной панели вы можете:
            - Просматривать список продуктов с полями 'user', 'product'.
    """

    list_display = ('user', 'product')


admin.site.register(Favorite, FavoriteAdmin)
