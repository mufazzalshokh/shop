# Generated by Django 3.2 on 2021-05-09 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authormodel',
            options={'verbose_name': 'author', 'verbose_name_plural': 'authors'},
        ),
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterModelOptions(
            name='posttagmodel',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
    ]
