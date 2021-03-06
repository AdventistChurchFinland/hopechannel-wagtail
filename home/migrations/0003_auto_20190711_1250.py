# Generated by Django 2.2.3 on 2019-07-11 12:50

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='promoted_series_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sub_title',
            field=models.CharField(default='Temp', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HomePageSeriesPreviewsOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_previews', to='home.HomePage')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.SeriesPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePagePromotedSeriesOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='promoted_series', to='home.HomePage')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.SeriesPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
