# Generated by Django 3.2.7 on 2021-09-09 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('team_name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=350)),
                ('condition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='items.item')),
            ],
        ),
    ]
