from django.db.models import QuerySet
from typing import Optional

from db.models import Movie


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids is not None:
        movies = movies.filter(genres__id__in=genres_ids).distinct()

    if actors_ids is not None:
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list] = None,
        actors_ids: Optional[list] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids is not None:
        for genre_id in genres_ids:
            movie.genres.add(genre_id)

    if actors_ids is not None:
        for actor_id in actors_ids:
            movie.actors.add(actor_id)

    return movie
