from wagtail.core import blocks


class PromotedSeriesBlock(blocks.StructBlock):
    """Promoted Series"""

    title = blocks.CharBlock(
        required=False, help_text="Title for the promoted series block")
    disable_info = blocks.BooleanBlock(
        required=False, help_text="Disable the display of series info (visible as default)")
    series = blocks.ListBlock(blocks.PageChooserBlock(
        label="Series", required=False, page_type='series.SeriesPage', can_choose_root=False))

    class Meta:  # noqa
        template = "series/promoted_series_block.html"
        icon = "media"
        label = "Promoted Series"


class SeriesPreviewBlock(blocks.StructBlock):
    """Series Preview"""

    title = blocks.CharBlock(
        required=False, help_text="Title for the series preview block")
    series = blocks.PageChooserBlock(
        label="Series", required=False, page_type='series.SeriesPage', can_choose_root=False)

    class Meta:  # noqa
        template = "series/series_preview_block.html"
        icon = "media"
        label = "Series Preview"
