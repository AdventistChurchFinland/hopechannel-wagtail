from django.db import models

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, RichTextField
from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.edit_handlers import ImageChooserPanel

from video.edit_handlers import VideoChooserPanel
from video.models import VideoSerializer


class MoviePage(Page):
    """Movie Page"""
    template = "movie/movie_page.html"

    video = models.ForeignKey(
        "video.Video",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    sub_title = models.CharField(blank=False, null=False, max_length=255)
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The hero image is used in the page header."
    )
    hover_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    year = models.PositiveIntegerField(null=False, blank=False)
    producer = models.CharField(blank=True, null=True, max_length=255)
    description = RichTextField(
        features=['h3', 'h4', 'ol', 'ul', 'bold', 'italic', 'link'], null=True, blank=True)

    api_fields = [
        APIField('sub_title'),
        APIField('hero', serializer=ImageRenditionField(
            'fill-1920x780')),
        APIField('video', serializer=VideoSerializer(
            'fill-1024x1024 ')),
        APIField('hover_thumbnail', serializer=ImageRenditionField(
            'fill-1024x1024 ')),
        APIField('year'),
        APIField('producer'),
        APIField('description'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            VideoChooserPanel('video'),
        ], heading="Video"),
        MultiFieldPanel([
            FieldPanel('sub_title'),
            ImageChooserPanel('hero'),
            ImageChooserPanel('hover_thumbnail'),
        ], heading="Header"),
        MultiFieldPanel([
            FieldPanel('producer'),
            FieldPanel('year'),
            FieldPanel('description'),
        ], heading="Information"),
    ]

    parent_page_types = ['movie.MoviesIndexPage']
    subpage_types = []

    def __str__(self):
        return self.title


class MoviesIndexPage(Page):
    """Movies index page"""
    template = "movie/movies_index.html"

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
        ], heading="Header")
    ]

    subpage_types = ['movie.MoviePage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["movies"] = MoviePage.objects.live().public()
        return context

    def __str__(self):
        return self.title
