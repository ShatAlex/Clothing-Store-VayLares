# Generated by Django 4.1.2 on 2023-02-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0011_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ManyToManyField(to='clothes.sizes_of_clothes', verbose_name='Товар'),
        ),
    ]
