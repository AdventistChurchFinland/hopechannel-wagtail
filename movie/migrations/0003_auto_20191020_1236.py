# Generated by Django 2.2.5 on 2019-10-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_moviepage_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviepage',
            old_name='produced',
            new_name='year',
        ),
        migrations.AddField(
            model_name='moviepage',
            name='producer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
