from utils import process_text, write_results_to_file


if __name__ == '__main__':
    filename = 'example.txt'  # Ваш шлях до файлу
    word_count, sentence_count = process_text(filename)

    output_filename = 'results.txt'  # Шлях до файлу для запису результатів
    write_results_to_file(output_filename, word_count, sentence_count)
    print(f"Результати записано у файл: {output_filename}")