# Generated by Django 3.2.13 on 2022-04-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20220413_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('image', models.FileField(blank=True, null=True, upload_to='uploads/pics')),
                ('Type', models.CharField(max_length=20)),
                ('discription', models.TextField()),
            ],
        ),
    ]