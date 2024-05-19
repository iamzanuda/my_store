# Generated by Django 5.0.4 on 2024-05-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Red', 'Красный')], help_text='Цвета продукта', max_length=50, verbose_name='Цвета'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(help_text='Загрузите изображение товара', upload_to='images/', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(choices=[('S', 'S, EUR: 38, RUS 44'), ('M', 'M, EUR: 40, RUS 46'), ('L', 'L, EUR: 42, RUS 48'), ('XL', 'XL, EUR: 44, RUS 50')], help_text='Размеры продукта', max_length=50, verbose_name='Размеры'),
        ),
    ]