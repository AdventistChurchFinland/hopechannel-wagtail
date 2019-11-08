from django.utils.functional import cached_property

from wagtail.core import blocks


class VideoChooserBlock(blocks.ChooserBlock):
    @cached_property
    def target_model(self):
        from .models import Video
        return Video

    @cached_property
    def widget(self):
        from .widgets import AdminVideoChooser
        return AdminVideoChooser

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
