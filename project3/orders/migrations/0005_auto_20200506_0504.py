# Generated by Django 3.0.5 on 2020-05-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200505_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='food', to='orders.Menu'),
        ),
    ]