# Generated by Django 5.0.6 on 2024-05-16 10:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0008_alter_order_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="product",
            new_name="products",
        ),
    ]
