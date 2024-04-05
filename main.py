import os
from utils import count_words_and_sentences


def main():
    # Get the file path
    file_path = os.path.join("example.txt")

    # Count words and sentences
    word_count, sentence_count = count_words_and_sentences(file_path)

    # Print the results
    if word_count is not None and sentence_count is not None:
        print("Number of words in the file:", word_count)
        print("Number of sentences in the file:", sentence_count)


if __name__ == "__main__":
    main()