from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

from video.edit_handlers import VideoChooserPanel


class HomePagePromotedSeriesOrderable(Orderable):
    """Allows selecting one or more series to display in the promoted series section"""

    page = ParentalKey("home.HomePage", related_name="promoted_series")
    series = models.ForeignKey("series.SeriesPage", on_delete=models.CASCADE)

    panels = [
        PageChooserPanel("series")
    ]


class HomePageSeriesPreviewsOrderable(Orderable):
    """Allows selecting one or more series to display in the promoted series section"""

    page = ParentalKey("home.HomePage", related_name="series_previews")
    title = models.CharField(blank=True, null=True, max_length=255)
    series = models.ForeignKey("series.SeriesPage", on_delete=models.CASCADE)

    panels = [
        FieldPanel("title"),
        PageChooserPanel("series"),
    ]


class HomePagePromotedMoviesOrderable(Orderable):
    """Allows selecting one or more series to display in the promoted series section"""

    page = ParentalKey("home.HomePage", related_name="promoted_movies")
    movie = models.ForeignKey("movie.MoviePage", on_delete=models.CASCADE)

    panels = [
        PageChooserPanel("movie"),
    ]


class HomePagePromotedVideosOrderable(Orderable):
    """Allows selecting one or more series to display in the promoted series section"""

    page = ParentalKey("home.HomePage", related_name="promoted_videos")
    video = models.ForeignKey("video.Video", on_delete=models.CASCADE)

    panels = [
        VideoChooserPanel('video'),
    ]


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
    promoted_series_title = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Title")
    promoted_movies_title = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Title")
    promoted_videos_title = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Title")
    promoted_videos_sub_title = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Sub title")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sub_title'),
            ImageChooserPanel('hero'),
        ], heading="Header"),
        MultiFieldPanel([
            FieldPanel('promoted_movies_title'),
            InlinePanel("promoted_movies", min_num=0, max_num=8)
        ], heading="Promoted Movies"),
        MultiFieldPanel([
            FieldPanel('promoted_videos_title'),
            FieldPanel('promoted_videos_sub_title'),
            InlinePanel("promoted_videos", min_num=0, max_num=8)
        ], heading="Promoted Videos"),
        MultiFieldPanel([
            FieldPanel('promoted_series_title'),
            InlinePanel("promoted_series", min_num=1, max_num=6)
        ], heading="Promoted Series"),
        MultiFieldPanel([
            InlinePanel("series_previews", min_num=1)
        ], heading="Series Previews"),
    ]
