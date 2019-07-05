from django.conf.urls import url

from .views import chooser

urlpatterns = [
    url(r'^chooser/$', chooser.chooser, name='chooser'),
    url(r'^chooser/(\d+)/$', chooser.video_chosen, name='video_chosen'),
]
