from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.contrib.modeladmin.mixins import ThumbnailMixin

from .models import Video


class VideoAdmin(ThumbnailMixin, ModelAdmin):
    """Channel Video Admin"""

    model = Video
    add_to_settings = False
    exclude_from_explorer = False
    menu_icon = 'media'
    menu_order = 200
    list_display = ("admin_thumb", "admin_title", "external_video_id",)
    list_filter = ("categories", "tags",)
    search_fields = ("external_video_id", "title", "tags",)
    list_display_add_buttons = 'admin_title'

    thumb_image_field_name = 'thumbnail'
    thumb_image_filter_spec = 'fill-80x45'
    thumb_image_width = 'auto'
    thumb_default = 'https://via.placeholder.com/80x45'
    thumb_col_header_text = _('thumbnail')

    def get_extra_class_names_for_field_col(self, obj, field_name):
        if field_name is 'admin_title':
            return ['title']
        return []

    def admin_title(self, obj):
        return mark_safe('<h2><a href="{}">{}</a></h2>'.format(
            self.url_helper.get_action_url('edit', obj.id),
            obj.title
        ))

    admin_title.short_description = 'Title'


modeladmin_register(VideoAdmin)
