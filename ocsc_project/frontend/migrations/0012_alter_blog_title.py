# Generated by Django 3.2.13 on 2022-04-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_auto_20220422_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
