
# BooksCollector — юнит-тесты

Проект содержит юнит-тесты для класса `BooksCollector`. Тесты написаны с помощью `pytest`
и покрывают все публичные методы класса. Каждый тест атомарный: проверяет один сценарий
поведения и может упасть только по одной причине.

## Структура тестов

Все тесты находятся в классе `TestBooksCollector`, общий экземпляр создаётся через фикстуру `collector`.

### add_new_book

- `test_add_new_book_valid_name_in_dict` — корректное название появляется в словаре (параметризовано: обычное имя, 40 и 39 символов).
- `test_add_new_book_increases_dict_size` — добавление книги увеличивает словарь ровно на одну запись.
- `test_add_new_book_empty_name_not_added` — книга с пустым названием не добавляется.
- `test_add_new_book_too_long_name_not_added` — книга с названием длиннее 40 символов не добавляется.
- `test_add_new_book_no_duplicates` — повторное добавление той же книги не создаёт дубликат.

### set_book_genre

- `test_set_book_genre_valid` — допустимый жанр устанавливается для существующей книги.
- `test_set_book_genre_book_not_exists` — для несуществующей книги жанр не устанавливается, словарь не меняется.
- `test_set_book_genre_invalid_genre` — жанр вне разрешённого списка не сохраняется.

### get_books_with_specific_genre

- `test_get_books_with_specific_genre_found` — возвращаются все книги запрошенного жанра.
- `test_get_books_with_specific_genre_not_found` — для несуществующего жанра возвращается пустой список.

### get_books_for_children

- `test_get_books_for_children_includes_safe_book` — книга без возрастного рейтинга попадает в список.
- `test_get_books_for_children_excludes_age_rated` — книги из списка с возрастным рейтингом исключаются (параметризовано: «Ужасы», «Детективы»).

### Работа с избранным

- `test_favorites_add_and_no_duplicates` — книга добавляется в избранное, дубликаты не попадают.
- `test_favorites_delete_existing_book` — существующая книга удаляется из избранного.
- `test_favorites_delete_nonexistent_book` — удаление несуществующей книги не выбрасывает исключение и не меняет список.

### get_books_genre

- `test_get_books_genre_returns_dict` — метод возвращает словарь.
- `test_get_books_genre_contains_all_books` — в словаре есть все добавленные книги.
- `test_get_books_genre_stores_genre` — в словаре хранится установленный жанр.

## Запуск тестов

```bash
pytest -v tests.py