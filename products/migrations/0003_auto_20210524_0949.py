# Generated by Django 3.2 on 2021-05-24 04:49

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210509_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='brandmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.brandmodel', verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(upload_to='products', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='long_description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.FloatField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='short_description',
            field=models.TextField(verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='products.ProductTagModel', verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='producttagmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='crated_at'),
        ),
        migrations.AlterField(
            model_name='producttagmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
