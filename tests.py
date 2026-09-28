from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # тест: добавление книг с валидными названиями, включая граничное значение (40 символов)
    def test_add_new_book_valid_names(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("1984")
        collector.add_new_book("a" * 40)  # ровно 40 символов — максимум

        assert "Война и мир" in collector.books_genre
        assert "1984" in collector.books_genre
        assert ("a" * 40) in collector.books_genre

    # параметризованный тест: недопустимые названия (пустое и слишком длинное)
    @pytest.mark.parametrize("name", ["", "x" * 41])
    def test_add_new_book_invalid_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # тест: нельзя добавить одну и ту же книгу дважды
    def test_add_new_book_no_duplicates(self):
        collector = BooksCollector()
        book = "Мастер и Маргарита"
        collector.add_new_book(book)
        collector.add_new_book(book)  # повторная попытка

        assert len(collector.books_genre) == 1
        assert book in collector.books_genre

    # тест: установка жанра для существующей книги
    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        book = "Дюна"
        genre = "Фантастика"
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    # тест: попытка установить жанр для книги, которой нет в словаре
    def test_set_book_genre_book_not_exists(self):
        collector = BooksCollector()
        invalid_book = "Неизвестная книга"
        genre = "Детективы"
        collector.set_book_genre(invalid_book, genre)
        assert invalid_book not in collector.books_genre

    # тест: получение книг по конкретному жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга А")
        collector.add_new_book("Книга Б")
        collector.add_new_book("Книга В")

        collector.set_book_genre("Книга А", "Фантастика")
        collector.set_book_genre("Книга Б", "Фантастика")
        collector.set_book_genre("Книга В", "Детективы")

        result = collector.get_books_with_specific_genre("Фантастика")
        assert set(result) == {"Книга А", "Книга Б"}

        empty_result = collector.get_books_with_specific_genre("Мультфильмы")
        assert empty_result == []

    # тест: работа с избранным — добавление и запрет дубликатов
    def test_favorites_add_and_no_duplicates(self):
        collector = BooksCollector()
        book = "Любимая книга"
        collector.add_new_book(book)

        collector.add_favorite_book(book)
        assert book in collector.get_list_of_favorites_books()

        collector.add_favorite_book(book)  # повторная попытка
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count(book) == 1

    # тест: удаление книги из избранного
    def test_favorites_delete_and_list(self):
        collector = BooksCollector()
        book1 = "Книга 1"
        book2 = "Книга 2"

        collector.add_new_book(book1)
        collector.add_new_book(book2)

        collector.add_favorite_book(book1)
        collector.add_favorite_book(book2)

        collector.delete_favorite_book(book1)

        favorites_after_delete = collector.get_list_of_favorites_books()
        assert book1 not in favorites_after_delete
        assert book2 in favorites_after_delete