# Generated by Django 5.0.1 on 2024-01-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_buy_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
