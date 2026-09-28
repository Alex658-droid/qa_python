import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    # 1. add_new_book: валидное добавление и проверка длины имени (параметризовано)
    @pytest.mark.parametrize("name, expected_len", [
        ("Книга А", 1),
        ("X" * 40, 1),          # ровно 40 символов
        ("X" * 39, 1),          # 39 символов
    ])
    def test_add_new_book_valid_names(self, collector, name, expected_len):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()
        assert len(collector.get_books_genre()) == expected_len

    # 2. add_new_book: недопустимые имена (пустое, слишком длинное)
    @pytest.mark.parametrize("name", [
        "",
        "X" * 41,
    ])
    def test_add_new_book_invalid_names(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    # 3. add_new_book: запрет дубликатов
    def test_add_new_book_no_duplicates(self, collector):
        name = "Книга А"
        collector.add_new_book(name)
        collector.add_new_book(name)  # повторный вызов
        # В словаре ключ уникален, но проверим, что не добавилось дважды (логика метода)
        assert collector.get_books_genre().get(name) == ""
        assert len(collector.get_books_genre()) == 1

    # 4. set_book_genre: установка допустимого жанра
    def test_set_book_genre_valid(self, collector):
        book_name = "Книга Б"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # 5. set_book_genre: книга не существует — ничего не происходит
    def test_set_book_genre_book_not_exists(self, collector):
        collector.set_book_genre("Не существующая книга", "Фантастика")
        # Словарь не должен измениться
        assert len(collector.get_books_genre()) == 0

    # 6. set_book_genre: недопустимый жанр (не из списка genre)
    def test_set_book_genre_invalid_genre(self, collector):
        book_name = "Книга В"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Неизвестный жанр")
        # Жанр не должен установиться (в текущей реализации просто не запишется)
        assert collector.get_book_genre(book_name) != "Неизвестный жанр"
        assert collector.get_book_genre(book_name) == ""

    # 7. get_books_with_specific_genre: книги по жанру + неверный жанр
    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Книга А", "Книга Б"]),
        ("Детективы", ["Книга В"]),
        ("Неизвестный", []),
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        collector.add_new_book("Книга А")
        collector.add_new_book("Книга Б")
        collector.add_new_book("Книга В")
        collector.set_book_genre("Книга А", "Фантастика")
        collector.set_book_genre("Книга Б", "Фантастика")
        collector.set_book_genre("Книга В", "Детективы")

        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    # 8. get_books_for_children: книги без возрастного рейтинга
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Детская книга")
        collector.add_new_book("Ужастик")
        collector.add_new_book("Детектив дня")

        collector.set_book_genre("Детская книга", "Мультфильмы")      # нет в age_rating
        collector.set_book_genre("Ужастик", "Ужасы")                  # есть в age_rating
        collector.set_book_genre("Детектив дня", "Детективы")         # есть в age_rating

        children_books = collector.get_books_for_children()
        assert "Детская книга" in children_books
        assert "Ужастик" not in children_books
        assert "Детектив дня" not in children_books

    # 9. Работа с избранным: добавление, запрет дублей, удаление
    def test_favorites_add_and_no_duplicates(self, collector):
        book = "Любимая книга"
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)  # повтор
        assert collector.get_list_of_favorites_books() == [book]

    def test_favorites_delete_and_list(self, collector):
        book = "Ещё одна книга"
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()
        # Удаление несуществующей — ничего не ломается
        collector.delete_book_from_favorites("Не существует")
        assert len(collector.get_list_of_favorites_books()) == 0

    # 10. get_books_genre: возвращаем весь словарь
    def test_get_books_genre(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Комедии")
        result = collector.get_books_genre()
        assert isinstance(result, dict)
        assert "Книга 1" in result
        assert "Книга 2" in result
        assert result["Книга 1"] == "Комедии"
        assert result["Книга 2"] == ""