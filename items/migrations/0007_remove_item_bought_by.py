# Generated by Django 3.2.7 on 2021-09-10 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_item_bought_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='bought_by',
        ),
    ]
