from wagtail.core import blocks

from video.models import VideoSerializer


class PromotedMoviesPageChooserBlock(blocks.PageChooserBlock):
    def get_api_representation(self, value, context=None):
        page_id = super().get_api_representation(value, context=context)

        video = VideoSerializer(
            'fill-1024x1024').to_representation(value.video)
        hover_thumbnail = value.hover_thumbnail.get_rendition('fill-1024x1024')

        return {
            'id': page_id,
            'title': value.title,
            'hover_thumbnail': hover_thumbnail.url,
            'producer': value.producer,
            'year': value.year,
            'video': video,
        }


class PromotedMoviesBlock(blocks.StructBlock):
    """Promoted Movies"""

    title = blocks.CharBlock(
        required=False, help_text="Title for the promoted movies block")
    movies = blocks.ListBlock(PromotedMoviesPageChooserBlock(
        label="Movies", required=False, page_type='movie.MoviePage', can_choose_root=False))

    class Meta:  # noqa
        template = "movie/promoted_movies_block.html"
        icon = "media"
        label = "Promoted Movies"
