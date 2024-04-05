from utils import process_text, count_words, count_sentences, write_results_to_file
from tempfile import NamedTemporaryFile
import pytest


# Тестові дані для функції count_sentences
@pytest.mark.parametrize("content,expected", [
    ("This is the first sentence. And this is the second!", 2),
    ("Will this... count as two sentences?", 2),
    ("Without ending", 0),
    ("One sentence! One more sentence. And one more?", 3),
    ("...?!!!", 5),
])
def test_count_sentences(content, expected):
    assert count_sentences(content) == expected, f"Помилка у функції count_sentences для тексту: {content}"


# Тестові дані для функції count_words
@pytest.mark.parametrize("content,expected", [
    ("These are four words.", 4),
    ("Spaces and tabs\t now", 4),
    ("", 0),
    ("Punctuation, does not affect: the number of words!", 8),
    ("One-two, three-four", 2),
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
    ("One. Two, three; four! Five?", 5, 3),
    ("No words, no sentences...", 4, 1),
    ("Just a sentence without punctuation", 5, 0),
    ("", 0, 0),  # Порожній файл
    ("One sentence. And one more... And one more!", 8, 3),
])
def test_process_text(create_temp_file, content, expected_word_count, expected_sentence_count):
    filename = create_temp_file(content)
    word_count, sentence_count = process_text(filename)
    assert word_count == expected_word_count, f"Очікувалось {expected_word_count} слів, але знайдено {word_count}"
    assert sentence_count == expected_sentence_count, f"Очікувалось {expected_sentence_count} речень, але знайдено {sentence_count}"



@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_output.txt"
@pytest.mark.parametrize("word_count,sentence_count,expected_content", [
    (5, 2, "Number of words: 5, Number of sentences: 2\n"),
    (0, 0, "Number of words: 0, Number of sentences: 0\n"),
    (100, 50, "Number of words: 100, Number of sentences: 50\n"),
])
def test_write_results_to_file(temp_file, word_count, sentence_count, expected_content):
    # Викликаємо функцію для запису результатів у тимчасовий файл
    write_results_to_file(temp_file, word_count, sentence_count)

    # Перевіряємо вміст файлу
    with open(temp_file, 'r', encoding='utf-8') as file:
        content = file.read()
        assert content == expected_content, f"Фактичний вміст файлу: {content}"