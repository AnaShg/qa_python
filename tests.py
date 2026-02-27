import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


# ---------------- add_new_book ----------------

def test_add_new_book_adds_book(collector):
    collector.add_new_book('Гарри Поттер')
    assert 'Гарри Поттер' in collector.books_genre


def test_add_new_book_does_not_add_duplicate(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Гарри Поттер')
    assert len(collector.books_genre) == 1


@pytest.mark.parametrize('name', [
    '',
    'A' * 41
])
def test_add_new_book_invalid_length(collector, name):
    collector.add_new_book(name)
    assert name not in collector.books_genre


# ---------------- set_book_genre ----------------

def test_set_book_genre_sets_valid_genre(collector):
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Фантастика')
    assert collector.get_book_genre('Книга') == 'Фантастика'


def test_set_book_genre_invalid_genre(collector):
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Несуществующий жанр')
    assert collector.get_book_genre('Книга') == ''


def test_set_book_genre_nonexistent_book(collector):
    collector.set_book_genre('Нет книги', 'Фантастика')
    assert collector.get_book_genre('Нет книги') is None


# ---------------- get_book_genre ----------------

def test_get_book_genre_returns_genre(collector):
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Комедии')
    assert collector.get_book_genre('Книга') == 'Комедии'


# ---------------- get_books_with_specific_genre ----------------

def test_get_books_with_specific_genre_returns_correct_books(collector):
    collector.add_new_book('Книга1')
    collector.add_new_book('Книга2')

    collector.set_book_genre('Книга1', 'Фантастика')
    collector.set_book_genre('Книга2', 'Комедии')

    result = collector.get_books_with_specific_genre('Фантастика')

    assert result == ['Книга1']


def test_get_books_with_specific_genre_invalid_genre(collector):
    result = collector.get_books_with_specific_genre('Несуществующий')
    assert result == []


# ---------------- get_books_genre ----------------

def test_get_books_genre_returns_dict(collector):
    assert isinstance(collector.get_books_genre(), dict)


# ---------------- get_books_for_children ----------------

def test_get_books_for_children_excludes_age_rating(collector):
    collector.add_new_book('Детская')
    collector.add_new_book('Ужасы')

    collector.set_book_genre('Детская', 'Мультфильмы')
    collector.set_book_genre('Ужасы', 'Ужасы')

    result = collector.get_books_for_children()

    assert 'Детская' in result
    assert 'Ужасы' not in result


# ---------------- add_book_in_favorites ----------------

def test_add_book_in_favorites_adds_book(collector):
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    assert 'Книга' in collector.get_list_of_favorites_books()


def test_add_book_in_favorites_does_not_add_twice(collector):
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.add_book_in_favorites('Книга')
    assert collector.get_list_of_favorites_books().count('Книга') == 1


def test_add_book_in_favorites_nonexistent_book(collector):
    collector.add_book_in_favorites('Нет книги')
    assert collector.get_list_of_favorites_books() == []


# ---------------- delete_book_from_favorites ----------------

def test_delete_book_from_favorites_removes_book(collector):
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.delete_book_from_favorites('Книга')
    assert 'Книга' not in collector.get_list_of_favorites_books()


# ---------------- get_list_of_favorites_books ----------------

def test_get_list_of_favorites_books_returns_list(collector):
    assert isinstance(collector.get_list_of_favorites_books(), list)