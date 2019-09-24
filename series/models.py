from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from video.edit_handlers import VideoChooserPanel


class SeriesPageRelatedSeries(Orderable):
    """Allows selecting one or more series to display in the related series section"""

    page = ParentalKey("series.SeriesPage", related_name="related_series",
                       on_delete=models.CASCADE, blank=True)
    series = models.ForeignKey(
        "series.SeriesPage", on_delete=models.CASCADE)

    panels = [
        PageChooserPanel("series")
    ]


class SeriesPage(Page):
    """Series page"""
    template = "series/series_page.html"

    sub_title = models.CharField(blank=False, null=False, max_length=255)
    produced_from = models.PositiveIntegerField(null=False, blank=False)
    produced_to = models.PositiveIntegerField(null=True, blank=True)
    description = RichTextField(
        features=['h3', 'h4', 'ol', 'ul', 'bold', 'italic', 'link'], null=True, blank=True)
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The hero image is used in the page header as well as in the information description of the series."
    )
    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The poster image is used in some promotional listings of the series."
    )
    related_series_title = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Title")
    multi_season_series = models.BooleanField(
        blank=True, null=False, default=False, verbose_name="Multi season series", help_text="Is this a part of a multi season series?")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sub_title'),
            ImageChooserPanel('hero'),
        ], heading="Header"),
        MultiFieldPanel([
            FieldPanel('description'),
            FieldPanel('produced_from'),
            FieldPanel('produced_to'),
            ImageChooserPanel('poster'),
            FieldPanel('multi_season_series'),
        ], heading="Information"),
        InlinePanel('episodes', label="Episodes"),
        MultiFieldPanel([
            FieldPanel('related_series_title'),
            InlinePanel("related_series", max_num=6)
        ], heading="Related Series"),
    ]

    @property
    def has_new_episodes(self):
        new_episodes = self.episodes.filter(is_new=True)
        return len(new_episodes) > 0

    parent_page_types = ['series.SeriesIndexPage']
    subpage_types = []

    def get_admin_display_title(self):
        return '{} – {}'.format(super().get_admin_display_title(), self.sub_title)

    def __str__(self):
        return self.title

    class Meta:  # noqa
        verbose_name_plural = "Series"


class SeriesEpisode(Orderable):
    """Episode class"""

    page = ParentalKey(
        "series.SeriesPage",
        on_delete=models.CASCADE,
        related_name="episodes"
    )
    video = models.ForeignKey(
        "video.Video",
        on_delete=models.CASCADE,
        related_name="+"
    )
    is_new = models.BooleanField(
        blank=True, null=False, default=False, verbose_name="New episode")

    panels = [
        VideoChooserPanel('video'),
        FieldPanel('is_new')
    ]

    def __str__(self):
        return self.series.title + ": " + self.video.title


class SeriesIndexPage(Page):
    """Series index page"""
    template = "series/series_index.html"

    sub_title = models.CharField(blank=False, null=False, max_length=255)
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sub_title'),
            ImageChooserPanel('hero'),
        ], heading="Header"),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['series.SeriesIndexPage', 'series.SeriesPage']

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["series"] = SeriesPage.objects.live().public()
        return context
