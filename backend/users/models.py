from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model that extends the AbstractUser class.
    This allows for additional customizations to the user model.
    """

    pass

    class Meta:
        """
        Meta class for defining model metadata.

        If you need to change the name or language of the table
        in the admin panel, uncomment the lines:
        -> verbose_name = ''
        -> verbose_name_plural = ''
        """

        # verbose_name = 'Пользователь'
        # verbose_name_plural = 'Пользователи'

    def __str__(self):
        """
        Возвращает имя пользователя.
        """

        return self.username
