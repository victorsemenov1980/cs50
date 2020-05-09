# Generated by Django 3.0.5 on 2020-05-05 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200504_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='order',
            name='toppings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
