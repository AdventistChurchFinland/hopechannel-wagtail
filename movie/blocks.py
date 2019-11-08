from wagtail.core import blocks


class PromotedMoviesBlock(blocks.StructBlock):
    """Promoted Movies"""

    title = blocks.CharBlock(
        required=False, help_text="Title for the promoted movies block")
    movies = blocks.ListBlock(blocks.PageChooserBlock(
        label="Movies", required=False, page_type='movie.MoviePage', can_choose_root=False))

    class Meta:  # noqa
        template = "movie/promoted_movies_block.html"
        icon = "media"
        label = "Promoted Movies"
