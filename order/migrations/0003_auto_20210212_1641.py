# Generated by Django 3.1.5 on 2021-02-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210212_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_paid',
            field=models.BooleanField(default=False),
        ),
    ]