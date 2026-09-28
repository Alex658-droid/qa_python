# BooksCollector — тесты на pytest

Реализованы юнит-тесты для класса `BooksCollector`.

## Список тестов

- `test_add_new_book_add_two_books` — проверка добавления двух книг и подсчёта количества через `get_books_rating()`.
- `test_add_new_book_valid_names` — добавление книг с корректными названиями, включая название длиной ровно 40 символов.
- `test_add_new_book_invalid_names` — параметризованный тест: проверка отклонения пустых названий и названий длиннее 40 символов.
- `test_add_new_book_no_duplicates` — проверка, что одну и ту же книгу нельзя добавить дважды.
- `test_set_book_genre_valid` — установка допустимого жанра для существующей книги.
- `test_set_book_genre_book_not_exists` — попытка установить жанр для несуществующей книги (ничего не происходит).
- `test_get_books_with_specific_genre` — получение списка книг по жанру; проверка пустого результата.
- `test_favorites_add_and_no_duplicates` — добавление книги в избранное и запрет дубликатов.
- `test_favorites_delete_and_list` — удаление книги из избранного и проверка актуального списка.

## Запуск тестов

```bash
pytest -v tests.py