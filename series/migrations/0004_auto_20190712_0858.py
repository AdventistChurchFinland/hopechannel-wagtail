# Generated by Django 2.2.3 on 2019-07-12 08:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20190712_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriespage',
            name='related_series_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.CreateModel(
            name='SeriesPageRelatedSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_series', to='series.SeriesPage')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.SeriesPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
