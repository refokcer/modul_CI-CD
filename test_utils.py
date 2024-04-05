from utils import process_text, count_words, count_sentences
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
