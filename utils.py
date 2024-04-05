def count_sentences(content: str) -> int:
    # Визначаємо символи, які закінчують речення
    sentence_endings = {'.', '!', '?'}
    sentence_count = sum(content.count(end) for end in sentence_endings)
    # Додаємо рахунок для '...', оскільки попередній підрахунок додав би 3 за кожне '...'
    additional_count = content.count('...')
    sentence_count -= 2 * additional_count
    return sentence_count


def count_words(content: str) -> int:
    # Визначаємо символи-розділювачі
    word_delimiters = {',', ' ', ':', ';'}
    # Підготовка тексту для підрахунку слів
    for delimiter in word_delimiters:
        content = content.replace(delimiter, ' ')
    # Рахуємо слова
    words = content.split()
    return len(words)


def process_text(filename: str) -> tuple[int, int]:
    # Читаємо вміст файлу
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Викликаємо функції для підрахунку слів та речень
    word_count = count_words(content)
    sentence_count = count_sentences(content)

    return word_count, sentence_count


def write_results_to_file(output_filename: str, word_count: int, sentence_count: int):
    """
    Записує результати підрахунку слів і речень у текстовий файл.

    :param output_filename: Шлях до файлу для запису результатів.
    :param word_count: Кількість слів.
    :param sentence_count: Кількість речень.
    """
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(f"Кількість слів: {word_count}, Кількість речень: {sentence_count}\n")