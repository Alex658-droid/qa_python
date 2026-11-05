import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    # 1. add_new_book: валидное имя попадает в словарь
    @pytest.mark.parametrize("name", [
        "Книга А",
        "X" * 40,          # ровно 40 символов
        "X" * 39,          # 39 символов
    ])
    def test_add_new_book_valid_name_in_dict(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # 1.1 add_new_book: добавление увеличивает словарь на одну запись
    @pytest.mark.parametrize("name", [
        "Книга А",
        "X" * 40,
        "X" * 39,
    ])
    def test_add_new_book_increases_dict_size(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    # 2. add_new_book: пустое имя не добавляется
    def test_add_new_book_empty_name_not_added(self, collector):
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    # 2.1 add_new_book: слишком длинное имя не добавляется
    def test_add_new_book_too_long_name_not_added(self, collector):
        name = "X" * 41
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    # 3. add_new_book: запрет дубликатов
    def test_add_new_book_no_duplicates(self, collector):
        name = "Книга А"
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    # 4. set_book_genre: установка допустимого жанра
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book("Книга Б")
        collector.set_book_genre("Книга Б", "Фантастика")
        assert collector.get_book_genre("Книга Б") == "Фантастика"

    # 5. set_book_genre: книга не существует — словарь не меняется
    def test_set_book_genre_book_not_exists(self, collector):
        collector.set_book_genre("Не существующая книга", "Фантастика")
        assert len(collector.get_books_genre()) == 0

    # 6. set_book_genre: недопустимый жанр не записывается
    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Книга В")
        collector.set_book_genre("Книга В", "Неизвестный жанр")
        assert collector.get_book_genre("Книга В") == ""

    # 7. get_books_with_specific_genre: книги нужного жанра
    def test_get_books_with_specific_genre_found(self, collector):
        for name in ("Книга А", "Книга Б", "Книга В"):
            collector.add_new_book(name)
        collector.set_book_genre("Книга А", "Фантастика")
        collector.set_book_genre("Книга Б", "Фантастика")
        collector.set_book_genre("Книга В", "Детективы")

        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга А", "Книга Б"]

    # 7.1 get_books_with_specific_genre: несуществующий жанр даёт пустой список
    def test_get_books_with_specific_genre_not_found(self, collector):
        collector.add_new_book("Книга А")
        collector.set_book_genre("Книга А", "Фантастика")

        assert collector.get_books_with_specific_genre("Неизвестный") == []

    # 8. get_books_for_children: книга без возрастного рейтинга попадает в список
    def test_get_books_for_children_includes_safe_book(self, collector):
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")

        assert "Детская книга" in collector.get_books_for_children()

    # 8.1 get_books_for_children: книги с возрастным рейтингом исключаются
    @pytest.mark.parametrize("name, genre", [
        ("Ужастик", "Ужасы"),
        ("Детектив дня", "Детективы"),
    ])
    def test_get_books_for_children_excludes_age_rated(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name not in collector.get_books_for_children()

    # 9. Работа с избранным: добавление и запрет дублей
    def test_favorites_add_and_no_duplicates(self, collector):
        book = "Любимая книга"
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    # 9.1 Удаление существующей книги из избранного
    def test_favorites_delete_existing_book(self, collector):
        book = "Ещё одна книга"
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert book not in collector.get_list_of_favorites_books()

    # 9.2 Удаление несуществующей книги не ломает список
    def test_favorites_delete_nonexistent_book(self, collector):
        collector.add_new_book("Любая книга")
        collector.add_book_in_favorites("Любая книга")

        collector.delete_book_from_favorites("Не существует")

        assert len(collector.get_list_of_favorites_books()) == 1

    # 10. get_books_genre: метод возвращает словарь
    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book("Книга 1")
        assert isinstance(collector.get_books_genre(), dict)

    # 10.1 get_books_genre: содержит все добавленные книги
    def test_get_books_genre_contains_all_books(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        result = collector.get_books_genre()

        assert "Книга 1" in result
        assert "Книга 2" in result

    # 10.2 get_books_genre: хранит установленный жанр
    def test_get_books_genre_stores_genre(self, collector):
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Комедии")

        assert collector.get_books_genre()["Книга 1"] == "Комедии"