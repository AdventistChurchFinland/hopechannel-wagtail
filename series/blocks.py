from collections import OrderedDict

from wagtail.core import blocks

from rest_framework.fields import Field

from video.models import VideoSerializer


class PromotedSeriesPageChooserBlock(blocks.PageChooserBlock):
    def get_api_representation(self, value, context=None):
        page_id = super().get_api_representation(value, context=context)

        hero_rendition = value.hero.get_rendition('fill-1920x780')
        poster_rendition = value.poster.get_rendition('width-218')

        return {
            'id': page_id,
            'title': value.title,
            'sub_title': value.sub_title,
            'description': value.description,
            'produced_from': value.produced_from,
            'produced_to': value.produced_to,
            'episode_count': value.episodes.count(),
            'hero_url': hero_rendition.url,
            'poster_url': poster_rendition.url,
        }


class PromotedSeriesBlock(blocks.StructBlock):
    """Promoted Series"""

    title = blocks.CharBlock(
        required=False, help_text="Title for the promoted series block")
    disable_info = blocks.BooleanBlock(
        required=False, help_text="Disable the display of series info (visible as default)")
    series = blocks.ListBlock(PromotedSeriesPageChooserBlock(
        label="Series", required=False, page_type='series.SeriesPage', can_choose_root=False))

    class Meta:  # noqa
        template = "series/promoted_series_block.html"
        icon = "media"
        label = "Promoted Series"


class EpisodeSerializer(Field):
    def to_representation(self, episode):
        video = VideoSerializer(
            'fill-512x288').to_representation(episode.video)

        return OrderedDict([
            ('sort_order', episode.sort_order),
            ('is_new', episode.is_new),
            ('video', video),
        ])


class SeriesPreviewPageChooserBlock(blocks.PageChooserBlock):
    def get_api_representation(self, value, context=None):
        page_id = super().get_api_representation(value, context=context)
        episodes = [EpisodeSerializer().to_representation(episode)
                    for episode in value.episodes.all()]
        return {
            'id': page_id,
            'url': value.url,
            'title': value.title,
            'sub_title': value.sub_title,
            'episodes': episodes,
        }


class SeriesPreviewBlock(blocks.StructBlock):
    """Series Preview"""

    title = blocks.CharBlock(
        required=False, help_text="Title for the series preview block")
    series = SeriesPreviewPageChooserBlock(
        label="Series", required=False, page_type='series.SeriesPage', can_choose_root=False)

    class Meta:  # noqa
        template = "series/series_preview_block.html"
        icon = "media"
        label = "Series Preview"
