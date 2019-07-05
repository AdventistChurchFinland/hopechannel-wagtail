from django.conf.urls import include, url
from django.urls import reverse
from django.utils.html import format_html

from wagtail.core import hooks

from video import admin_urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^video/', include((admin_urls, 'video'), namespace='video')),
    ]


@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script>
            window.chooserUrls.videoChooser = '{0}';
        </script>
        """,
        reverse('video:chooser')
    )
