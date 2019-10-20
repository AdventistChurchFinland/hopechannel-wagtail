# Generated by Django 2.2.5 on 2019-10-20 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_video_rating'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviepage',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='video.Video'),
            preserve_default=False,
        ),
    ]
