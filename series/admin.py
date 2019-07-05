from django.utils.safestring import mark_safe

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from video.admin import VideoAdmin

from .models import Series


class SeriesAdmin(ModelAdmin):
    """Channel Series Admin"""

    model = Series
    add_to_settings = False
    exclude_from_explorer = False
    menu_icon = 'doc-full-inverse'
    menu_order = 300
    list_display = ("admin_title",)
    search_fields = ("title",)

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


modeladmin_register(SeriesAdmin)
