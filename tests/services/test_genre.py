from unittest.mock import MagicMock
import pytest

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService
from setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    test_genre1 = Genre(id=1, name='test_genre1')
    test_genre2 = Genre(id=2, name='test_genre2')
    test_genre3 = Genre(id=3, name='test_genre3')

    genre_dao.get_one = MagicMock(return_value=test_genre1)
    genre_dao.get_all = MagicMock(return_value=[test_genre1, test_genre2, test_genre3])

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all(None)
        assert len(genres) > 0
        assert len(genres) == 3
