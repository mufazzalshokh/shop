# Generated by Django 3.2 on 2021-06-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210609_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='real_price',
            field=models.FloatField(default=0, verbose_name='real price'),
        ),
    ]
