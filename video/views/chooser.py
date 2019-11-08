from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.admin.modal_workflow import render_modal_workflow
from wagtail.admin.utils import PermissionPolicyChecker
from wagtail.core.models import Collection

from video.admin import VideoAdmin
from video.models import Video

if WAGTAIL_VERSION < (2, 5):
    from wagtail.admin.forms import SearchForm
else:
    from wagtail.admin.forms.search import SearchForm


def get_video_thumbnail_url(thumbnail):
    if thumbnail is None:
        return None

    return thumbnail.get_rendition('max-165x165').url


def get_video_json(video):
    """
    helper function: given a media, return the json to pass back to the
    chooser panel
    """

    video_modeladmin = VideoAdmin()

    return {
        'id': video.id,
        'title': video.title,
        'thumbnail': get_video_thumbnail_url(video.thumbnail),
        'edit_link': video_modeladmin.url_helper.get_action_url('edit', video.id)
    }


def chooser(request):
    video_files = []

    q = None
    is_searching = False
    if 'q' in request.GET or 'p' in request.GET:
        video_files = Video.objects.all()

        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            q = searchform.cleaned_data['q']

            video_files = video_files.search(q)
            is_searching = True
        else:
            video_files = video_files.order_by('-title')
            is_searching = False

        # Pagination
        paginator = Paginator(video_files, per_page=10)
        page = paginator.get_page(request.GET.get('p'))

        return render(request, "video/chooser/results.html", {
            'video_files': video_files,
            'query_string': q,
            'is_searching': is_searching,
        })
    else:
        searchform = SearchForm()

        video_files = Video.objects.order_by('-title')
        paginator = Paginator(video_files, per_page=10)

    video_modeladmin = VideoAdmin()

    return render_modal_workflow(request, 'video/chooser/chooser.html', None, {
        'video_files': video_files,
        'searchform': searchform,
        'is_searching': False,
        'video_index_url': video_modeladmin.url_helper.index_url,
    }, json_data={
        'step': 'chooser',
        'error_label': "Server Error",
        'error_message': "Report this error to your webmaster with the following information:",
    })


def video_chosen(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    return render_modal_workflow(
        request, None, None,
        None,
        json_data={'step': 'video_chosen', 'result': get_video_json(video)}
    )
