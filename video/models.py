from collections import OrderedDict

from django import forms
from django.db import models, IntegrityError
from django.utils.text import slugify

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.search.queryset import SearchableQuerySetMixin
from wagtail.snippets.models import register_snippet

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from rest_framework.serializers import Field


@register_snippet
class VideoCategory(models.Model):
    """Media Category class."""

    name = models.CharField(blank=False, null=False, max_length=255)
    slug = models.SlugField(blank=True, null=False, unique=True,
                            max_length=255, editable=False)

    panels = [
        FieldPanel('name'),
    ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        iteration = 1
        while True:
            try:
                return super(VideoCategory, self).save(*args, **kwargs)
            except IntegrityError:
                self.slug = '-'.join(slugify(self.name), iteration)
                iteration += iteration

    def __str__(self):
        return self.name

    class Meta:  # noqa
        verbose_name_plural = "Video Categories"
        ordering = ["name"]


class MediaQuerySet(SearchableQuerySetMixin, models.QuerySet):
    pass


class VideoTag(TaggedItemBase):
    content_object = models.ForeignKey(
        'video.Video', related_name="tagged_items", on_delete=models.CASCADE)


class Video(index.Indexed, models.Model):
    """Video class"""

    external_video_id = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        unique=True,
    )
    title = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    rating = models.CharField(null=True, blank=True, max_length=5)
    duration = models.DurationField(
        blank=True, null=True, help_text="Insert duration either as minutes, e.g. `127` or as a time string e.g. `2:07`.")
    categories = models.ManyToManyField("video.VideoCategory", blank=True)
    tags = TaggableManager(through=VideoTag, blank=True)

    objects = MediaQuerySet.as_manager()

    search_fields = [
        index.SearchField('external_video_id'),
        index.SearchField('title', partial_match=True, boost=10),
    ]

    panels = [
        FieldPanel('external_video_id', classname="title"),
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('description', widget=forms.Textarea),
            ImageChooserPanel('thumbnail'),
        ], heading="Basic information"),
        MultiFieldPanel([
            FieldPanel('duration'),
            FieldPanel('rating'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Details")
    ]

    def duration_string(self):
        seconds = self.duration.seconds

        minutes = seconds // 60
        seconds = seconds % 60

        return '{:02d}:{:02d}'.format(minutes, seconds)

    def __str__(self):
        return self.title


class VideoSerializer(Field):
    def __init__(self, filter_spec, *args, **kwargs):
        self.filter_spec = filter_spec
        super(VideoSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, video):
        thumbnail_rendition = video.thumbnail.get_rendition(self.filter_spec)

        return OrderedDict([
            ('external_video_id', video.external_video_id),
            ('title', video.title),
            ('description', video.description),
            ('thumbnail', thumbnail_rendition.url),
            ('rating', video.rating),
            ('duration', video.duration.total_seconds()),
        ])
