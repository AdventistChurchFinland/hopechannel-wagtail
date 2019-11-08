from collections import OrderedDict

from django.db import models

from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.api import APIField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from rest_framework.serializers import ModelSerializer

from video.edit_handlers import VideoChooserPanel
from video.models import VideoSerializer

from .blocks import PromotedSeriesBlock


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
    multi_season_series = models.BooleanField(
        blank=True, null=False, default=False, verbose_name="Multi season series", help_text="Is this a part of a multi season series?")
    content = StreamField([
        ('related_series', PromotedSeriesBlock()),
    ], null=True, blank=True)

    api_fields = [
        APIField('sub_title'),
        APIField('produced_from'),
        APIField('produced_to'),
        APIField('description'),
        APIField('hero', serializer=ImageRenditionField(
            'fill-1920x780')),
        APIField('poster', serializer=ImageRenditionField(
            'width-218')),
        APIField('episodes'),
        APIField('content'),
    ]

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
        StreamFieldPanel('content'),
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

    api_fields = [
        APIField('video', serializer=VideoSerializer('fill-512x288')),
        APIField('is_new'),
    ]

    panels = [
        VideoChooserPanel('video'),
        FieldPanel('is_new'),
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

    api_fields = [
        APIField('sub_title'),
        APIField('hero', serializer=ImageRenditionField(
            'fill-1920x780')),
    ]

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


class EpisodeSerializer(ModelSerializer):
    video = VideoSerializer('fill-512x288')

    class Meta:
        model = SeriesEpisode
        fields = [
            'sort_order',
            'is_new',
            'video',
        ]


class SeriesPreviewSerializer(ModelSerializer):
    episodes = EpisodeSerializer(many=True)

    class Meta:
        model = SeriesPage
        fields = [
            'id',
            'url',
            'title',
            'sub_title',
            'episodes',
        ]
