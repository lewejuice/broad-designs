# Generated by Django 3.1.5 on 2021-02-19 08:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210217_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
