# Generated by Django 4.1.2 on 2023-02-01 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_sizes_clothes_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizes',
            name='count',
        ),
    ]
