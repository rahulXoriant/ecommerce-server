# Generated by Django 3.2.19 on 2023-05-22 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
    ]
