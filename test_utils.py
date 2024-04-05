from utils import process_text, count_words, count_sentences
from tempfile import NamedTemporaryFile
import pytest


# Тестові дані для функції count_sentences
@pytest.mark.parametrize("content,expected", [
    ("Це перше речення. І це друге!", 2),
    ("Чи буде це... рахуватися як два речення?", 2),
    ("Без закінчення", 0),
    ("Одне речення! Ще одне речення. І ще одне?", 3),
    ("...?!!!", 5),
])
def test_count_sentences(content, expected):
    assert count_sentences(content) == expected, f"Помилка у функції count_sentences для тексту: {content}"


# Тестові дані для функції count_words
@pytest.mark.parametrize("content,expected", [
    ("Це три слова.", 3),
    ("Пробіли    і табуляції\tзараз", 4),
    ("", 0),
    ("Пунктуація, не впливає: на; кількість? слів!", 6),
    ("Одне-два, три-чотири", 2),
])
def test_count_words(content, expected):
    assert count_words(content) == expected, f"Помилка у функції count_words для тексту: {content}"


# Фікстура для створення тимчасового файлу з заданим вмістом
@pytest.fixture
def create_temp_file():
    def _create_temp_file(content):
        with NamedTemporaryFile('w+', encoding='utf-8', delete=False) as tmpfile:
            tmpfile.write(content)
            tmpfile.flush()
            return tmpfile.name

    return _create_temp_file


# Параметризований тест для функції process_text
@pytest.mark.parametrize("content,expected_word_count,expected_sentence_count", [
    ("Один. Два, три; чотири! П'ять?", 5, 3),
    ("Без слів без речень...", 4, 1),
    ("Просто речення без знаків пунктуації", 5, 0),
    ("", 0, 0),  # Порожній файл
    ("Одне речення. І ще одне... І ще одне!", 8, 3),
])
def test_process_text(create_temp_file, content, expected_word_count, expected_sentence_count):
    filename = create_temp_file(content)
    word_count, sentence_count = process_text(filename)
    assert word_count == expected_word_count, f"Очікувалось {expected_word_count} слів, але знайдено {word_count}"
    assert sentence_count == expected_sentence_count, f"Очікувалось {expected_sentence_count} речень, але знайдено {sentence_count}"