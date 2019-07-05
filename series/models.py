from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from video.edit_handlers import VideoChooserPanel


class Series(ClusterableModel):
    """Series class"""

    title = models.CharField(blank=False, null=False, max_length=255)
    sub_title = models.CharField(blank=False, null=False, max_length=255)
    produced_from = models.PositiveIntegerField(null=False, blank=False)
    produced_to = models.PositiveIntegerField(null=True, blank=True)
    description = RichTextField(
        features=['h3', 'h4', 'ol', 'ul', 'bold', 'italic', 'link'])
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        FieldPanel('title', classname="title"),
        MultiFieldPanel([
            FieldPanel('sub_title'),
            FieldPanel('description'),
            FieldPanel('produced_from'),
            FieldPanel('produced_to'),
        ], heading="Information"),
        MultiFieldPanel([
            ImageChooserPanel('hero'),
            ImageChooserPanel('poster'),
        ], heading="Images"),
        InlinePanel('episodes', label="Episode")
    ]

    def __str__(self):
        return self.title

    class Meta:  # noqa
        verbose_name_plural = "Series"


class SeriesEpisode(models.Model):
    """Episode class"""

    page = ParentalKey(
        Series,
        on_delete=models.CASCADE,
        related_name="episodes"
    )
    video = models.ForeignKey(
        "video.Video",
        on_delete=models.CASCADE,
        related_name="+"
    )
    episode_number = models.PositiveIntegerField(null=False, blank=False)

    panels = [
        VideoChooserPanel('video'),
        FieldPanel('episode_number')
    ]

    def __str__(self):
        return self.series.title + ": " + self.video.title


class SeriesPage(Page):
    """Series page"""
    template = "series/series_page.html"

    series = models.ForeignKey(
        'series.Series',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('series'),
    ]

    parent_page_types = ['series.SeriesIndexPage']
    subpage_types = ['series.SeriesIndexPage', 'series.SeriesPage']


class SeriesIndexOrderable(Orderable):
    """Allows selecting one or more series to display in the series index page"""
    page = ParentalKey("series.SeriesIndexPage", related_name="series")
    series = models.ForeignKey("series.Series", on_delete=models.CASCADE)

    panels = [
        FieldPanel("series")
    ]


class SeriesIndexPage(Page):
    """Series index page"""

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel('series')

            ], heading="Series"
        )
    ]

    parent_page_types = []
    subpage_types = ['series.SeriesIndexPage', 'series.SeriesPage']
