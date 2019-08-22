# Generated by Django 2.2.4 on 2019-08-22 09:45

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.search.index


class Migration(migrations.Migration):

    replaces = [('video', '0001_initial'), ('video', '0002_auto_20190705_0808'), ('video', '0003_auto_20190705_0853'), ('video', '0004_auto_20190712_0743'), ('video', '0005_auto_20190712_0752'), ('video', '0006_auto_20190712_0858')]

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Video Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_video_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('categories', models.ManyToManyField(blank=True, to='video.VideoCategory')),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='VideoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='video.Video')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_videotag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='video.VideoTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.DurationField(blank=True, help_text='Insert duration either as minutes, e.g. `127` or as a time string e.g. `2:07`.', null=True),
        ),
    ]
