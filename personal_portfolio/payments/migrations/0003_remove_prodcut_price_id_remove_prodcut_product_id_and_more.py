# Generated by Django 5.0.6 on 2024-07-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_prodcut_detail_prodcut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodcut',
            name='price_id',
        ),
        migrations.RemoveField(
            model_name='prodcut',
            name='product_id',
        ),
        migrations.AlterField(
            model_name='prodcut',
            name='price',
            field=models.IntegerField(max_length=3),
        ),
    ]
