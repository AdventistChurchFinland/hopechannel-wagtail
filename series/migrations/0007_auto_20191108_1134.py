# Generated by Django 2.2.7 on 2019-11-08 09:34

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_auto_20191108_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriespage',
            name='content',
            field=wagtail.core.fields.StreamField([('related_series', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title for the promoted series block', required=False)), ('disable_info', wagtail.core.blocks.BooleanBlock(help_text='Disable the display of series info (visible as default)', required=False)), ('series', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(can_choose_root=False, label='Series', page_type=['series.SeriesPage'], required=False)))]))], blank=True, null=True),
        ),
    ]
