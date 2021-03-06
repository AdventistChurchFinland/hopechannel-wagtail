# Generated by Django 2.2.4 on 2019-08-22 09:56

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    replaces = [('series', '0001_initial'), ('series', '0002_auto_20190712_0707'), ('series', '0003_auto_20190712_0743'), ('series', '0004_auto_20190712_0858'), ('series',
                                                                                                                                                                  '0005_auto_20190712_0900'), ('series', '0006_auto_20190712_0903'), ('series', '0007_remove_seriesepisode_episode_number'), ('series', '0008_auto_20190712_0924')]

    initial = True

    dependencies = [
        ('video', '0003_auto_20190705_0853'),
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                  parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero', models.ForeignKey(blank=True, null=True,
                                           on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('sub_title', models.CharField(default='Temp', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SeriesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                  parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('sub_title', models.CharField(max_length=255)),
                ('produced_from', models.PositiveIntegerField()),
                ('produced_to', models.PositiveIntegerField(blank=True, null=True)),
                ('description', wagtail.core.fields.RichTextField(
                    blank=True, null=True)),
                ('hero', models.ForeignKey(blank=True, help_text='The hero image is used in the page header as well as in the information description of the series.',
                                           null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('poster', models.ForeignKey(blank=True, help_text='The poster image is used in some promotional listings of the series.',
                                             null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('related_series_title', models.CharField(blank=True,
                                                          max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SeriesPageRelatedSeries',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(
                    blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                                         related_name='related_series', to='series.SeriesPage')),
                ('series', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='series.SeriesPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SeriesEpisode',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='series.SeriesPage')),
                ('video', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='+', to='video.Video')),
                ('sort_order', models.IntegerField(
                    blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
    ]
