# Generated by Django 5.0.1 on 2024-01-11 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('discription', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_to_buy_list.itemtype')),
            ],
        ),
    ]
