# Generated by Django 3.1.5 on 2021-03-10 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210203_0956'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Portfolio_category',
        ),
    ]
