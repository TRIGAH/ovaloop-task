# Generated by Django 5.0.6 on 2024-05-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_product_business_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metameasurement",
            name="full_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
