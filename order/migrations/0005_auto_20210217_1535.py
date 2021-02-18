# Generated by Django 3.1.5 on 2021-02-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210213_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='project_services',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_paid',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
