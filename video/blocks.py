from django.utils.functional import cached_property

from wagtail.core import blocks
from .models import VideoSerializer


class VideoChooserBlock(blocks.ChooserBlock):
    @cached_property
    def target_model(self):
        from .models import Video
        return Video

    @cached_property
    def widget(self):
        from .widgets import AdminVideoChooser
        return AdminVideoChooser

    def get_api_representation(self, value, context=None):
        video_id = super().get_api_representation(value, context=context)
        return VideoSerializer('fill-512x288').to_representation(value)

    class Meta:
        icon = "media"


class PromotedVideosBlock(blocks.StructBlock):
    """Promoted Movies"""

    title = blocks.CharBlock(
        required=False, help_text="Title for the promoted videos block")
    sub_title = blocks.CharBlock(
        required=False, help_text="Sub title for the promoted videos block")
    videos = blocks.ListBlock(VideoChooserBlock(
        label="Videos", required=False))

    class Meta:  # noqa
        template = "video/promoted_videos_block.html"
        icon = "media"
        label = "Promoted Videos"
