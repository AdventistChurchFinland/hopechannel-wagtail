# Generated by Django 2.2.3 on 2019-07-05 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videotype',
            options={'verbose_name_plural': 'Video Types'},
        ),
        migrations.AlterField(
            model_name='video',
            name='video_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='video.VideoType'),
        ),
    ]
