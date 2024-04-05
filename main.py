import os
from utils import process_text


if __name__ == '__main__':
    filename = 'example.txt'  # Ваш шлях до файлу
    word_count, sentence_count = process_text(filename)
    print(f"Кількість слів: {word_count}, Кількість речень: {sentence_count}")