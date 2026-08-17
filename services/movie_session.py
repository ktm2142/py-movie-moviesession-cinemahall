from datetime import datetime
from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str | None = None
) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(
            show_time__date=session_date
        )
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> QuerySet:
    fields_to_update = {
        "show_time": show_time,
        "cinema_hall_id": cinema_hall_id,
        "movie_id": movie_id
    }
    data = {
        key: value
        for key, value in fields_to_update.items()
        if value is not None
    }
    queryset = MovieSession.objects.filter(
        pk=session_id
    )
    queryset.update(**data)
    return queryset


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(pk=session_id).delete()
