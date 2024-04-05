def count_words_and_sentences(file_path: str) -> tuple[int, int]:
    """
    This function reads the content of a ".txt" file and returns the number of words and sentences in the file.

    Args:
        file_path: Path to the ".txt" file.

    Returns:
        Tuple: Number of words (int) and number of sentences (int).
    """
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read the file content
            text = file.read()
            words = 0
            sentences = 0
            for word in text.split():
                if word:
                    words += 1

            for punctuation in [".", "!", "?", "..."]:
                sentences += text.count(punctuation)

            return words, sentences
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)