from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.api import APIField
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.edit_handlers import ImageChooserPanel

from movie.blocks import PromotedMoviesBlock

from series.blocks import PromotedSeriesBlock, SeriesPreviewBlock

from video.blocks import PromotedVideosBlock


class HomePage(Page):
    """HomePage class"""

    template = "home/home_page.html"
    max_count = 1

    sub_title = models.CharField(blank=False, null=False, max_length=255)
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content = StreamField([
        ('promoted_series', PromotedSeriesBlock()),
        ('series_preview', SeriesPreviewBlock()),
        ('promoted_movies', PromotedMoviesBlock()),
        ('promoted_videos', PromotedVideosBlock()),
    ], null=True, blank=True)

    api_fields = [
        APIField('sub_title'),
        APIField('hero', serializer=ImageRenditionField(
            'fill-1920x780')),
        APIField('content'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sub_title'),
            ImageChooserPanel('hero'),
        ], heading="Header"),
        StreamFieldPanel('content'),
    ]
