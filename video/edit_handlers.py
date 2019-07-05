from __future__ import absolute_import, unicode_literals

from wagtail.admin.edit_handlers import BaseChooserPanel

from .widgets import AdminVideoChooser


class VideoChooserPanel(BaseChooserPanel):
    object_type_name = 'video'

    def widget_overrides(self):
        return {self.field_name: AdminVideoChooser}
