# Generated by Django 2.2.5 on 2019-10-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191020_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='promoted_videos_sub_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Sub title'),
        ),
    ]
