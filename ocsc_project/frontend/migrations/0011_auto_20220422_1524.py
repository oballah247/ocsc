# Generated by Django 3.2.13 on 2022-04-22 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0010_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
        migrations.AddField(
            model_name='blog',
            name='poster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
