# Generated by Django 3.1.5 on 2021-02-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20210219_1655',),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2021-02-19 06:00:00.000000-08:00'),
        ),
    ]