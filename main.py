

class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        # Доступные жанры
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        # Жанры с возрастным рейтингом (не подходят детям)
        self.genre_age_rating = ['Ужасы', 'Детективы']

    # Добавляем новую книгу: имя до 40 символов, дубликаты не добавляем
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # Устанавливаем жанр книги, если книга есть и жанр разрешён
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # Получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # Возвращаем список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # Возвращаем весь словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # Возвращаем книги, подходящие детям (без возрастного рейтинга)
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            # Жанр должен быть в списке разрешённых и не в списке с возрастным рейтингом
            if genre and genre in self.genre and genre not in self.genre_age_rating:
                books_for_children.append(name)
        return books_for_children

    # Добавляем книгу в избранное (если она есть и ещё не в избранном)
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # Удаляем книгу из избранного (если она там есть)
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # Получаем список избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites