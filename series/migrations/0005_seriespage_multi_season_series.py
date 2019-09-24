# Generated by Django 2.2.5 on 2019-09-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_auto_20190906_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriespage',
            name='multi_season_series',
            field=models.BooleanField(blank=True, default=False, help_text='Is this a part of a multi season series?', verbose_name='Multi season series'),
        ),
    ]
