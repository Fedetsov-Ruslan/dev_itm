# Generated by Django 4.2.7 on 2024-03-23 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='quantite',
            new_name='quantity',
        ),
    ]
