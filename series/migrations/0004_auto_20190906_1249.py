# Generated by Django 2.2.5 on 2019-09-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20190906_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriesepisode',
            name='is_new',
            field=models.BooleanField(blank=True, default=False, verbose_name='New episode'),
        ),
    ]
