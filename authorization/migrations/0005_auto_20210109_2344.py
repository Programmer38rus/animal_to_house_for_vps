# Generated by Django 3.1.2 on 2021-01-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_auto_20210109_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='561478', unique=True),
        ),
    ]
