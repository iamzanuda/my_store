from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Административная панель для управления отзывами.

    Attributes:
        list_display (tuple): Поля модели, отображаемые в списке отзывов.

    Examples:
        В административной панели вы можете:
            - Просматривать список продуктов с полями 'user', 'product',
              'rating', 'created_at'.
    """

    list_display = ('user', 'product', 'rating', 'created_at')


admin.site.register(Review, ReviewAdmin)
