import pytest


# ==================== add_new_book ====================

def test_add_new_book_adds_book_to_dictionary(collector):
    collector.add_new_book('Гарри Поттер')
    assert 'Гарри Поттер' in collector.books_genre


def test_add_new_book_does_not_add_duplicate(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Гарри Поттер')
    assert len(collector.books_genre) == 1


@pytest.mark.parametrize('name', ['', 'A' * 41])
def test_add_new_book_invalid_length(collector, name):
    collector.add_new_book(name)
    assert name not in collector.books_genre


# ==================== set_book_genre ====================

def test_set_book_genre_changes_dictionary_value(collector):
    collector.books_genre['Книга'] = ''
    collector.set_book_genre('Книга', 'Фантастика')
    assert collector.books_genre['Книга'] == 'Фантастика'


def test_set_book_genre_invalid_genre_does_not_change_value(collector):
    collector.books_genre['Книга'] = ''
    collector.set_book_genre('Книга', 'Несуществующий жанр')
    assert collector.books_genre['Книга'] == ''


# ==================== get_book_genre ====================

def test_get_book_genre_returns_correct_value(collector):
    collector.books_genre['Книга'] = 'Комедии'
    assert collector.get_book_genre('Книга') == 'Комедии'


def test_get_book_genre_nonexistent_book_returns_none(collector):
    assert collector.get_book_genre('Нет книги') is None


# ==================== get_books_with_specific_genre ====================

def test_get_books_with_specific_genre_returns_correct_books(collector):
    collector.books_genre = {
        'Книга1': 'Фантастика',
        'Книга2': 'Комедии'
    }
    result = collector.get_books_with_specific_genre('Фантастика')
    assert result == ['Книга1']


def test_get_books_with_specific_genre_invalid_genre_returns_empty_list(collector):
    assert collector.get_books_with_specific_genre('Несуществующий') == []


# ==================== get_books_genre ====================

def test_get_books_genre_returns_correct_dictionary(collector):
    collector.books_genre = {'Книга': 'Фантастика'}
    assert collector.get_books_genre() == {'Книга': 'Фантастика'}


# ==================== get_books_for_children ====================

def test_get_books_for_children_excludes_age_restricted_genre(collector):
    collector.books_genre = {
        'Детская': 'Мультфильмы',
        'Ужасы': 'Ужасы'
    }
    result = collector.get_books_for_children()
    assert 'Детская' in result
    assert 'Ужасы' not in result


# ==================== add_book_in_favorites ====================

def test_add_book_in_favorites_adds_book(collector):
    collector.books_genre['Книга'] = ''
    collector.add_book_in_favorites('Книга')
    assert 'Книга' in collector.favorites


def test_add_book_in_favorites_does_not_add_duplicate(collector):
    collector.books_genre['Книга'] = ''
    collector.favorites = ['Книга']
    collector.add_book_in_favorites('Книга')
    assert collector.favorites.count('Книга') == 1


def test_add_book_in_favorites_nonexistent_book_not_added(collector):
    collector.add_book_in_favorites('Нет книги')
    assert collector.favorites == []


# ==================== delete_book_from_favorites ====================

def test_delete_book_from_favorites_removes_book(collector):
    collector.favorites = ['Книга']
    collector.delete_book_from_favorites('Книга')
    assert 'Книга' not in collector.favorites


# ==================== get_list_of_favorites_books ====================

def test_get_list_of_favorites_books_returns_correct_list(collector):
    collector.favorites = ['Книга']
    assert collector.get_list_of_favorites_books() == ['Книга']