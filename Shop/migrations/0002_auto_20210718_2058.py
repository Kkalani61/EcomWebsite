# Generated by Django 3.1.7 on 2021-07-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='General', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
