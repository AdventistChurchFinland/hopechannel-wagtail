from __future__ import absolute_import, unicode_literals

import json

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.widgets import AdminChooser

from video.admin import VideoAdmin
from video.models import Video


class AdminVideoChooser(AdminChooser):
    choose_one_text = _("Choose a video")
    choose_another_text = _("Choose another video")
    link_to_chosen_text = _("Edit this video")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def render_html(self, name, value, attrs):
        instance, value = self.get_instance_and_id(Video, value)
        original_field_html = super(
            AdminVideoChooser, self).render_html(name, value, attrs)

        video_modeladmin = VideoAdmin()

        return render_to_string('video/widgets/video_chooser.html', {
            'widget': self,
            'original_field_html': original_field_html,
            'attrs': attrs,
            'value': value,
            'video': instance,
            'foo': 'bar',
            'edit_link': video_modeladmin.url_helper.get_action_url('edit', value)
        })

    def render_js_init(self, id_, name, value):
        return "createVideoChooser({0});".format(json.dumps(id_))

    class Media:
        js = [
            'video/js/video-chooser-modal.js',
            'video/js/video-chooser.js',
        ]
        css = {
            'all': ['video/css/video-chooser.css']
        }
