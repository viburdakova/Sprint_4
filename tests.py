import pytest

from qa_python.main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Гарри Поттер и Философский камень")
        collector.add_new_book("Гарри Поттер и Тайная комната")
        assert "Гарри Поттер и Философский камень" in collector.get_books_genre()

    @pytest.mark.parametrize("name, genre", [
        ("Властелин колец. Братство кольца", "Фантастика"),
        ("Король Лев", "Мультфильмы")
    ])

    def test_set_book_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre(self, collector):
        collector.add_new_book("Убийство на улице Морг")
        collector.set_book_genre("Убийство на улице Морг", "Детективы")
        assert collector.get_book_genre("Убийство на улице Морг") == "Детективы"

    def test_check_added_books_have_no_genres(self, collector):
        name = ["1984", "Анна Каренина", "Маленькие женщины"]
        for book_name in name:
            collector.add_new_book(book_name)
            assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")

        collector.add_new_book("ОНО")
        collector.set_book_genre("ОНО", "Ужасы")

        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние','ОНО']

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Кэрри")
        collector.set_book_genre("Кэрри", "Ужасы")

        collector.add_new_book("Корпорация монстров")
        collector.set_book_genre("Корпорация монстров", "Мультфильмы")

        assert collector.get_books_for_children() == ["Корпорация монстров"]

    def test_age_rated_books_not_in_children_list(self, collector):
        collector.add_new_book("Молчание ягнят")
        collector.set_book_genre("Молчание ягнят", "Ужасы")

        collector.add_new_book("Маленький принц")
        collector.set_book_genre("Маленький принц", "Фантастика")

        assert "Молчание ягнят" not in collector.get_books_for_children()
        assert "Маленький принц" in collector.get_books_for_children()

    def test_add_and_delete_favorite(self, collector):
        collector.add_new_book("Бойцовский клуб")
        collector.add_book_in_favorites("Бойцовский клуб")

        assert "Бойцовский клуб" in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites("Бойцовский клуб")

        assert "Избранная Книга" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self,collector):
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("name", [
        "Мастер и Маргарита",
        "Война и мир",
    ])
    def test_add_to_favorites(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()