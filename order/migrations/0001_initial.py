# Generated by Django 3.1.5 on 2021-02-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=50)),
                ('project_description', models.CharField(blank=True, max_length=99999, null=True)),
                ('target_audience', models.CharField(blank=True, max_length=10, null=True)),
                ('useful_links', models.CharField(blank=True, max_length=99999, null=True)),
                ('img_file', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]