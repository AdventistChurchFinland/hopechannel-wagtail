# Generated by Django 2.2.5 on 2019-10-25 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20191020_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviepage',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='video.Video'),
        ),
    ]