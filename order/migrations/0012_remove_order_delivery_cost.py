# Generated by Django 3.1.5 on 2021-02-23 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20210222_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_cost',
        ),
    ]
