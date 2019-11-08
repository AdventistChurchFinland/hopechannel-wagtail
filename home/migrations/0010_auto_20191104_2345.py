# Generated by Django 2.2.7 on 2019-11-04 21:45

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191104_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('promoted_series', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title for the promoted series block', required=False)), ('series', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('series', wagtail.core.blocks.PageChooserBlock(can_choose_root=False, label='Series', page_type=['series.SeriesPage'], required=True))])))]))], blank=True, null=True),
        ),
    ]